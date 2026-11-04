"""Tests for source-backed STL/3MF relationships and avoiding false print claims."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from component_review import analyze_links, make_report, resolve_used_meshes

def stl(fid, sha):
    return {"file_id":fid,"type":"STL","filename":fid+"_Part.stl",
            "path":"Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/"+fid+"_Part.stl",
            "geometry":{"translation_invariant_geometry_hash":sha}}

def job(fid, objects, build):
    obj=[{"id":str(i),"mesh":{"translation_invariant_geometry_hash":sha},"components":[]}
         for i,sha in objects.items()]
    return {"file_id":fid,"type":"3MF","filename":fid+"_Set.3mf",
            "path":"Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/"+fid+"_Set.3mf",
            "project":{"model_parts":[{"objects":obj,"build_items":[{"object_id":str(x)} for x in build]}],
                       "available_slicer_settings":{},"settings_sources":[]}}
class ComponentReviewTests(unittest.TestCase):
    def test_only_built_objects_count(self):
        data=[stl("3DP-1-101","AAA"),stl("3DP-1-102","BBB"),
              job("3DP-1-103",{1:"AAA",2:"BBB"},[1])]
        links, stl_jobs, dup=analyze_links(data)
        self.assertEqual(links["3DP-1-103"]["matching_stl_ids"],["3DP-1-101"])
        self.assertFalse(stl_jobs.get("3DP-1-102"))
    def test_partial_project_is_flagged(self):
        data=[stl("3DP-1-101","AAA"),job("3DP-1-103",{1:"AAA",2:"UNKNOWN"},[1,2])]
        links,_,_=analyze_links(data)
        self.assertEqual(links["3DP-1-103"]["unmatched_meshes"],1)
    def test_name_based_relationship_is_explicitly_not_exact(self):
        data=[stl("3DP-1-101","AAA"),job("3DP-1-102",{1:"CHANGED"},[1])]
        data[0]["filename"]="3DP-1-101_Front-Leg.stl"
        data[1]["filename"]="3DP-1-102_Front-Leg.3mf"
        links, stl_jobs, _=analyze_links(data)
        self.assertEqual(links["3DP-1-102"]["same_name_stl_ids"],["3DP-1-101"])
        self.assertFalse(links["3DP-1-102"]["matching_stl_ids"])
        self.assertFalse(stl_jobs.get("3DP-1-101"))
    def test_composed_build_item_resolves_child(self):
        p={"objects":[{"id":"1","mesh":None,"components":[{"object_id":"2"}]},
                      {"id":"2","mesh":{"translation_invariant_geometry_hash":"AAA"},"components":[]}],
           "build_items":[{"object_id":"1"}]}
        used,warnings=resolve_used_meshes(p)
        self.assertEqual(len(used),1)
        self.assertFalse(warnings)
    def test_report_does_not_infer_printing_approval(self):
        text,stats=make_report([stl("3DP-1-101","AAA"),job("3DP-1-102",{1:"AAA"},[1])])
        self.assertIn("not approval",text.lower())
        self.assertEqual(stats["fully_matched_jobs"],1)
if __name__=="__main__":
    unittest.main()
