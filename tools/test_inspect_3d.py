"""Regression checks for true moved holes and geometry-preserving translation."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from inspect_3d import mesh_stats, compare, changed_mesh_regions

def voxel_surface(hole_x):
    solid = {(x,y,z) for x in range(8) for y in range(8) for z in range(3)
             if not (x == hole_x and y == 3)}
    faces = []
    directions = [
        ((1,0,0), ((1,0,0),(1,1,0),(1,1,1),(1,0,1))),
        ((-1,0,0), ((0,0,0),(0,0,1),(0,1,1),(0,1,0))),
        ((0,1,0), ((0,1,0),(0,1,1),(1,1,1),(1,1,0))),
        ((0,-1,0), ((0,0,0),(1,0,0),(1,0,1),(0,0,1))),
        ((0,0,1), ((0,0,1),(1,0,1),(1,1,1),(0,1,1))),
        ((0,0,-1), ((0,0,0),(0,1,0),(1,1,0),(1,0,0)))
    ]
    for x,y,z in sorted(solid):
        for delta,quad in directions:
            if (x+delta[0],y+delta[1],z+delta[2]) in solid:
                continue
            pts = [tuple(float(coord+offset) for coord,offset in zip((x,y,z),v)) for v in quad]
            faces.extend(((pts[0],pts[1],pts[2]),(pts[0],pts[2],pts[3])))
    return faces

class GeometryChecks(unittest.TestCase):
    def test_whole_model_translation_preserves_normalized_mesh(self):
        a = voxel_surface(2)
        b = [tuple(tuple(v + (10 if i==0 else 4) for i,v in enumerate(p)) for p in tri) for tri in a]
        sa, sb = mesh_stats(a),mesh_stats(b)
        self.assertEqual(sa["translation_invariant_geometry_hash"],sb["translation_invariant_geometry_hash"])
        self.assertNotEqual(sa["bbox_min"], sb["bbox_min"])
    def test_hole_relocation_changes_mesh_even_with_identical_summary_metrics(self):
        a,b = mesh_stats(voxel_surface(2)),mesh_stats(voxel_surface(5))
        self.assertEqual(a["bbox_size"],b["bbox_size"])
        self.assertEqual(a["triangle_count"],b["triangle_count"])
        self.assertAlmostEqual(a["surface_area_model_units_squared"],b["surface_area_model_units_squared"])
        self.assertAlmostEqual(a["signed_volume_model_units_cubed"],b["signed_volume_model_units_cubed"])
        self.assertNotEqual(a["translation_invariant_geometry_hash"],b["translation_invariant_geometry_hash"])
        result = compare({"file_id":"a","geometry":a},{"file_id":"b","geometry":b})
        self.assertFalse(result["same_normalized_triangle_mesh"])
    def test_changed_region_reveals_hole_move(self):
        a, b = voxel_surface(2), voxel_surface(5)
        diff = changed_mesh_regions(a, b)
        self.assertGreater(diff["changed_regions_old"]["changed_triangles"], 0)
        self.assertGreater(diff["changed_regions_new"]["changed_triangles"], 0)
        self.assertIsNotNone(diff["changed_regions_old"]["region_bbox"])
        self.assertLessEqual(diff["changed_regions_old"]["region_extent"][0], 8)
    def test_translated_mesh_has_no_local_changed_triangles(self):
        a = voxel_surface(2)
        translated = [tuple(tuple(v+(3 if k == 0 else 8) for k, v in enumerate(p)) for p in tri) for tri in a]
        diff = changed_mesh_regions(a, translated)
        self.assertEqual(diff["changed_regions_old"]["changed_triangles"], 0)
        self.assertEqual(diff["changed_regions_new"]["changed_triangles"], 0)
    def test_watertight_through_hole_is_topologically_visible(self):
        a = mesh_stats(voxel_surface(2))
        self.assertTrue(a["watertight_edge_test"])
        self.assertEqual(a["through_tunnel_genus_estimate"],1)

if __name__ == "__main__":
    unittest.main()
