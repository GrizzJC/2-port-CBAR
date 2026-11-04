# Component and Print-Job Review — Automatically Generated

**Technical evidence only, not approval or proof of mechanical fit.**
This report groups all registered STL/3MF files by function and compares
actual STL meshes to mesh objects referenced by 3MF build items.
An exact translation-normalized geometry match is strong evidence
of the same triangular mesh at 0.0001 model-coordinate precision.
It is NOT proof that a physical print was completed or installed.

## At a glance

| Check | Count |
| --- | ---: |
| STL component files | 71 |
| 3MF print projects | 41 |
| Jobs with every referenced mesh matching an STL | 12 |
| Jobs partially matched to STL meshes | 3 |
| Jobs without exact matching STL geometry | 26 |
| STL files without an exact built-object 3MF match | 43 |
| No-exact-match 3MF projects with a same-name STL candidate | 23 |
| Jobs matching multiple distinct STL IDs | 3 |
| Identical-geometry STL ID groups | 1 |
| Parsing errors | 0 |

## Changes from the latest triggering push

No actual engineering asset or inventory change in this push.

## Priority review questions

1. Inspect every 3MF with unmatched or unresolved build geometry in the original slicer.
2. Confirm which STL parts belong in multipart jobs and how many copies are needed.
3. Check STL models without an exact 3MF match; they may be deliberately standalone.
4. Compare genuinely repeated meshes before proposing a deletion or renamed design.
5. Verify physical fit, actual printing settings, successful prints and approvals manually.

## Full inventory and associations

### 01 Behavioral Chamber

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-1-101 | [3DP-1-101_Front-Legs-I.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-101_Front-Legs-I.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-1-102 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-102 | [3DP-1-102_Front-Legs-I.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-102_Front-Legs-I.stl) | No exact 3MF job match; possible same-name print job 3DP-1-101 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-103 | [3DP-1-103_Front-Legs-II.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-103_Front-Legs-II.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-1-104 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-104 | [3DP-1-104_Front-Legs-II.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-104_Front-Legs-II.stl) | No exact 3MF job match; possible same-name print job 3DP-1-103 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-105 | [3DP-1-105_Rear-Legs-I.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-105_Rear-Legs-I.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-1-106 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-106 | [3DP-1-106_Rear-Legs-I.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/01-Cage-Structure/3DP-1-106_Rear-Legs-I.stl) | No exact 3MF job match; possible same-name print job 3DP-1-105 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-201 | [3DP-1-201_Cage-Alignment-Large.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/02-Cage-Alignment/3DP-1-201_Cage-Alignment-Large.stl) | Exact mesh in 3DP-1-202 | Confirm function, design revision and physical compatibility |
| 3DP-1-202 | [3DP-1-202_Cage-Alignment-Set.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/02-Cage-Alignment/3DP-1-202_Cage-Alignment-Set.3mf) | 7 build item(s); 7 built mesh reference(s); STL: 3DP-1-201, 3DP-1-203 | Confirm multi-part count, fit and slicer settings |
| 3DP-1-203 | [3DP-1-203_Cage-Alignment-small.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/02-Cage-Alignment/3DP-1-203_Cage-Alignment-small.stl) | Exact mesh in 3DP-1-202 | Confirm function, design revision and physical compatibility |
| 3DP-1-301 | [3DP-1-301_Top-Handle.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-301_Top-Handle.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-1-302 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-302 | [3DP-1-302_Top-Handle.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-302_Top-Handle.stl) | No exact 3MF job match; possible same-name print job 3DP-1-301 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-303 | [3DP-1-303_Top-Lock-Keepers.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-303_Top-Lock-Keepers.3mf) | 4 build item(s); 4 built mesh reference(s); no exact STL match; 4 unmatched; possible same-name STL: 3DP-1-304 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-304 | [3DP-1-304_Top-Lock-Keepers.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-304_Top-Lock-Keepers.stl) | No exact 3MF job match; possible same-name print job 3DP-1-303 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-305 | [3DP-1-305_Top-Lock-Latches.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-305_Top-Lock-Latches.3mf) | 4 build item(s); 4 built mesh reference(s); no exact STL match; 4 unmatched; possible same-name STL: 3DP-1-306 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-1-306 | [3DP-1-306_Top-Lock-Latches.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-306_Top-Lock-Latches.stl) | No exact 3MF job match; possible same-name print job 3DP-1-305 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-1-307 | [3DP-1-307_Top-Lock-Pivot-Mount.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-307_Top-Lock-Pivot-Mount.3mf) | 4 build item(s); 4 built mesh reference(s); STL: 3DP-1-308 | Confirm copies, fit and slicer settings |
| 3DP-1-308 | [3DP-1-308_Top-Lock-Pivot-Mount.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/03-Lid-and-Locks/3DP-1-308_Top-Lock-Pivot-Mount.stl) | Exact mesh in 3DP-1-307 | Confirm function, design revision and physical compatibility |
| 3DP-1-401 | [3DP-1-401_pee-tray-corner-1.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/04-Waste-Tray/3DP-1-401_pee-tray-corner-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-1-402 | [3DP-1-402_pee-tray-corner-2.stl](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/04-Waste-Tray/3DP-1-402_pee-tray-corner-2.stl) | Exact mesh in 3DP-1-403 | Confirm function, design revision and physical compatibility |
| 3DP-1-403 | [3DP-1-403_pee-tray-corners.3mf](../Rig-Engineering-Files/01-Behavioral-Chamber/3D-Printing/04-Waste-Tray/3DP-1-403_pee-tray-corners.3mf) | 4 build item(s); 4 built mesh reference(s); STL: 3DP-1-402; 2 unmatched | Inspect unmatched/absent print-project geometry; compare similar-size meshes |

### 02 Stimulus Presentation and Access

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-2-101 | [3DP-2-101_Frame-Tower-Foot.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/01-Delivery-Frame/3DP-2-101_Frame-Tower-Foot.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-2-102 | Confirm copies, fit and slicer settings |
| 3DP-2-102 | [3DP-2-102_Frame-Tower-Foot.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/01-Delivery-Frame/3DP-2-102_Frame-Tower-Foot.stl) | Exact mesh in 3DP-2-101 | Confirm function, design revision and physical compatibility |
| 3DP-2-103 | [3DP-2-103_Frame-Tower-Top-Brackets-Set.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/01-Delivery-Frame/3DP-2-103_Frame-Tower-Top-Brackets-Set.3mf) | 4 build item(s); 4 built mesh reference(s); no exact STL match; 4 unmatched | Inspect unmatched/absent print-project geometry |
| 3DP-2-104 | [3DP-2-104_frame-tower-top-left-bracket.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/01-Delivery-Frame/3DP-2-104_frame-tower-top-left-bracket.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-2-105 | [3DP-2-105_frame-tower-top-right-bracket.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/01-Delivery-Frame/3DP-2-105_frame-tower-top-right-bracket.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-2-201 | [3DP-2-201_Center-Door-and-Vac-Rail-Attachment.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-201_Center-Door-and-Vac-Rail-Attachment.3mf) | 3 build item(s); 3 built mesh reference(s); no exact STL match; 3 unmatched; possible same-name STL: 3DP-2-202 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-202 | [3DP-2-202_Center-Door-and-Vac-Rail-Attachment.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-202_Center-Door-and-Vac-Rail-Attachment.stl) | No exact 3MF job match; possible same-name print job 3DP-2-201 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-203 | [3DP-2-203_Center-Door-Top-Bracket.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-203_Center-Door-Top-Bracket.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-2-204 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-204 | [3DP-2-204_Center-Door-Top-Bracket.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-204_Center-Door-Top-Bracket.stl) | No exact 3MF job match; possible same-name print job 3DP-2-203 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-205 | [3DP-2-205_Lateral-Door-Rail-Attachment.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-205_Lateral-Door-Rail-Attachment.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-2-206 | [3DP-2-206_Lateral-Door-Top-Bracket.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-206_Lateral-Door-Top-Bracket.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-2-207 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-207 | [3DP-2-207_Lateral-Door-Top-Bracket.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-207_Lateral-Door-Top-Bracket.stl) | No exact 3MF job match; possible same-name print job 3DP-2-206 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-208 | [3DP-2-208_Linear-Actuator-Center-Door-Mount.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-208_Linear-Actuator-Center-Door-Mount.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-2-209 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-209 | [3DP-2-209_Linear-Actuator-Center-Door-Mount.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-209_Linear-Actuator-Center-Door-Mount.stl) | No exact 3MF job match; possible same-name print job 3DP-2-208 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-210 | [3DP-2-210_Linear-Actuator-Lateral-Door-Mount.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-210_Linear-Actuator-Lateral-Door-Mount.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-2-211 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-211 | [3DP-2-211_Linear-Actuator-Lateral-Door-Mount.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/02-Access-Doors-and-Actuators/3DP-2-211_Linear-Actuator-Lateral-Door-Mount.stl) | No exact 3MF job match; possible same-name print job 3DP-2-210 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-301 | [3DP-2-301_Single-Spout-Barrel-PLA.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/03-Spout-Bodies-and-Spacers/3DP-2-301_Single-Spout-Barrel-PLA.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-2-302 | Confirm copies, fit and slicer settings |
| 3DP-2-302 | [3DP-2-302_Single-Spout-Barrel-PLA.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/03-Spout-Bodies-and-Spacers/3DP-2-302_Single-Spout-Barrel-PLA.stl) | Exact mesh in 3DP-2-301 | Confirm function, design revision and physical compatibility |
| 3DP-2-303 | [3DP-2-303_Spout-Spacer-shorter-spout.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/03-Spout-Bodies-and-Spacers/3DP-2-303_Spout-Spacer-shorter-spout.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-2-304 | Confirm copies, fit and slicer settings |
| 3DP-2-304 | [3DP-2-304_Spout-Spacer-shorter-spout.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/03-Spout-Bodies-and-Spacers/3DP-2-304_Spout-Spacer-shorter-spout.stl) | Exact mesh in 3DP-2-303 | Confirm function, design revision and physical compatibility |
| 3DP-2-401 | [3DP-2-401_spout-clamp-to-mount-bracket.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-401_spout-clamp-to-mount-bracket.3mf) | 3 build item(s); 3 built mesh reference(s); STL: 3DP-2-402 | Confirm copies, fit and slicer settings |
| 3DP-2-402 | [3DP-2-402_Spout-clamp-to-mount-bracket.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-402_Spout-clamp-to-mount-bracket.stl) | Exact mesh in 3DP-2-401 | Confirm function, design revision and physical compatibility |
| 3DP-2-403 | [3DP-2-403_Spout-Mount-Assembly.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-403_Spout-Mount-Assembly.3mf) | 3 build item(s); 3 built mesh reference(s); no exact STL match; 3 unmatched; possible same-name STL: 3DP-2-404 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-404 | [3DP-2-404_Spout-Mount-Assembly.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-404_Spout-Mount-Assembly.stl) | No exact 3MF job match; possible same-name print job 3DP-2-403 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-405 | [3DP-2-405_Teflon-Tube-Spout-Clamp.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-405_Teflon-Tube-Spout-Clamp.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-2-406 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-2-406 | [3DP-2-406_Teflon-Tube-Spout-Clamp.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/04-Spout-Mounts-and-Clamps/3DP-2-406_Teflon-Tube-Spout-Clamp.stl) | No exact 3MF job match; possible same-name print job 3DP-2-405 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-2-501 | [3DP-2-501_Teflon-Tube-Vac-Hole-Tool.3mf](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/05-Spout-Tools-and-Alignment/3DP-2-501_Teflon-Tube-Vac-Hole-Tool.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-2-502 | Confirm copies, fit and slicer settings |
| 3DP-2-502 | [3DP-2-502_Teflon-Tube-Vac-Hole-Tool.stl](../Rig-Engineering-Files/02-Stimulus-Presentation-and-Access/3D-Printing/05-Spout-Tools-and-Alignment/3DP-2-502_Teflon-Tube-Vac-Hole-Tool.stl) | Exact mesh in 3DP-2-501 | Confirm function, design revision and physical compatibility |

### 03 Stimulus Storage and Selection

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-3-201 | [3DP-3-201_3-way-rod-connector.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-201_3-way-rod-connector.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-3-202 | [3DP-3-202_Chromaflex-Column-Clamp.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-202_Chromaflex-Column-Clamp.3mf) | 3 build item(s); 3 built mesh reference(s); no exact STL match; 3 unmatched; possible same-name STL: 3DP-3-203 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-3-203 | [3DP-3-203_Chromaflex-Column-Clamp.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-203_Chromaflex-Column-Clamp.stl) | No exact 3MF job match; possible same-name print job 3DP-3-202 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-3-204 | [3DP-3-204_Chromaflex-Rinse-Column-Holder.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-204_Chromaflex-Rinse-Column-Holder.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-3-205 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-3-205 | [3DP-3-205_Chromaflex-Rinse-Column-Holder.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-205_Chromaflex-Rinse-Column-Holder.stl) | No exact 3MF job match; possible same-name print job 3DP-3-204 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-3-206 | [3DP-3-206_Slot-Rail-Connecting-Bracket-for-Chromaflex-Rinse-Column-Holder.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-206_Slot-Rail-Connecting-Bracket-for-Chromaflex-Rinse-Column-Holder.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched | Inspect unmatched/absent print-project geometry |
| 3DP-3-207 | [3DP-3-207_Stimulus-Frame-Backbone.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-207_Stimulus-Frame-Backbone.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-3-208 | Confirm copies, fit and slicer settings |
| 3DP-3-208 | [3DP-3-208_Stimulus-Frame-Backbone.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-208_Stimulus-Frame-Backbone.stl) | Exact mesh in 3DP-3-207 | Confirm function, design revision and physical compatibility |
| 3DP-3-209 | [3DP-3-209_Stimulus-Frame-Backbone-End.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-209_Stimulus-Frame-Backbone-End.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-3-210 | Confirm copies, fit and slicer settings |
| 3DP-3-210 | [3DP-3-210_Stimulus-Frame-Backbone-End.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-210_Stimulus-Frame-Backbone-End.stl) | Exact mesh in 3DP-3-209 | Confirm function, design revision and physical compatibility |
| 3DP-3-211 | [3DP-3-211_Stimulus-Frame-Base-End.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-211_Stimulus-Frame-Base-End.3mf) | 3 build item(s); 3 built mesh reference(s); no exact STL match; 3 unmatched; possible same-name STL: 3DP-3-212 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-3-212 | [3DP-3-212_Stimulus-Frame-Base-End.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-212_Stimulus-Frame-Base-End.stl) | No exact 3MF job match; possible same-name print job 3DP-3-211 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-3-213 | [3DP-3-213_Syringe-Holder.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-213_Syringe-Holder.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-3-214 | Confirm copies, fit and slicer settings |
| 3DP-3-214 | [3DP-3-214_Syringe-Holder.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-214_Syringe-Holder.stl) | Exact mesh in 3DP-3-213 | Confirm function, design revision and physical compatibility |
| 3DP-3-215 | [3DP-3-215_Syringe-Holder-Top.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-215_Syringe-Holder-Top.3mf) | 1 build item(s); 1 built mesh reference(s); STL: 3DP-3-216 | Confirm copies, fit and slicer settings |
| 3DP-3-216 | [3DP-3-216_Syringe-Holder-Top.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-216_Syringe-Holder-Top.stl) | Exact mesh in 3DP-3-215 | Confirm function, design revision and physical compatibility |
| 3DP-3-217 | [3DP-3-217_Top-right-angle-and-3-way-rod-connector.3mf](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-217_Top-right-angle-and-3-way-rod-connector.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; approximate size candidates: 3DP-3-201, 3DP-3-218 | Inspect unmatched/absent print-project geometry; compare similar-size meshes |
| 3DP-3-218 | [3DP-3-218_Top-right-angle-rod-connector.stl](../Rig-Engineering-Files/03-Stimulus-Storage-and-Selection/3D-Printing/02-Syringe-and-Chromaflex-Holders/3DP-3-218_Top-right-angle-rod-connector.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |

### 04 Valves and Sound Attenuation

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-4-101 | [3DP-4-101_Valve-Sound-Attenuation-Chamber-Lid-Base.3mf](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-101_Valve-Sound-Attenuation-Chamber-Lid-Base.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-4-102 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-4-102 | [3DP-4-102_Valve-Sound-Attenuation-Chamber-Lid-Base.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-102_Valve-Sound-Attenuation-Chamber-Lid-Base.stl) | No exact 3MF job match; possible same-name print job 3DP-4-101 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-4-103 | [3DP-4-103_Valve-Sound-Attenuation-Chamber-Lid-Cap.3mf](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-103_Valve-Sound-Attenuation-Chamber-Lid-Cap.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-4-104 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-4-104 | [3DP-4-104_Valve-Sound-Attenuation-Chamber-Lid-Cap.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-104_Valve-Sound-Attenuation-Chamber-Lid-Cap.stl) | No exact 3MF job match; possible same-name print job 3DP-4-103 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-4-105 | [3DP-4-105_Valve-Sound-Attenuation-Chamber-Lid-Sides.3mf](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-105_Valve-Sound-Attenuation-Chamber-Lid-Sides.3mf) | 4 build item(s); 4 built mesh reference(s); no exact STL match; 4 unmatched; possible same-name STL: 3DP-4-106 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-4-106 | [3DP-4-106_Valve-Sound-Attenuation-Chamber-Lid-Sides.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/01-Valve-Sound-Attenuation-Chamber/3DP-4-106_Valve-Sound-Attenuation-Chamber-Lid-Sides.stl) | No exact 3MF job match; possible same-name print job 3DP-4-105 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-4-201 | [3DP-4-201_All-Valve-Driver-Case-Components.3mf](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/02-Valve-Driver-and-Hardware/3DP-4-201_All-Valve-Driver-Case-Components.3mf) | 2 build item(s); 2 built mesh reference(s); STL: 3DP-4-203; 1 unmatched | Inspect unmatched/absent print-project geometry; compare similar-size meshes |
| 3DP-4-202 | [3DP-4-202_Valve-Driver-Case.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/02-Valve-Driver-and-Hardware/3DP-4-202_Valve-Driver-Case.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-4-203 | [3DP-4-203_Valve-Driver-Cover.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/02-Valve-Driver-and-Hardware/3DP-4-203_Valve-Driver-Cover.stl) | Exact mesh in 3DP-4-201 | Confirm function, design revision and physical compatibility |
| 3DP-4-301 | [3DP-4-301_Stimulus-Frame-To-Valve-Chamber-Connecting-Bracket.3mf](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/03-Valve-Interfaces-and-Mounts/3DP-4-301_Stimulus-Frame-To-Valve-Chamber-Connecting-Bracket.3mf) | 2 build item(s); 2 built mesh reference(s); no exact STL match; 2 unmatched; possible same-name STL: 3DP-4-302 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-4-302 | [3DP-4-302_Stimulus-Frame-To-Valve-Chamber-Connecting-Bracket.stl](../Rig-Engineering-Files/04-Valves-and-Sound-Attenuation/3D-Printing/03-Valve-Interfaces-and-Mounts/3DP-4-302_Stimulus-Frame-To-Valve-Chamber-Connecting-Bracket.stl) | No exact 3MF job match; possible same-name print job 3DP-4-301 | Compare likely STL/3MF pair; meshes differ despite matching names |

### 05 Vacuum Gas and Drainage

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-5-101 | [3DP-5-101_Barbed-Fitting-Spout-Vac-Adaptor-0-25in-to-0-75in.3mf](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/01-Vacuum-and-Air-Fittings/3DP-5-101_Barbed-Fitting-Spout-Vac-Adaptor-0-25in-to-0-75in.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-5-102 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-5-102 | [3DP-5-102_Barbed-Fitting-Spout-Vac-Adaptor-0-25in-to-0-75in.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/01-Vacuum-and-Air-Fittings/3DP-5-102_Barbed-Fitting-Spout-Vac-Adaptor-0-25in-to-0-75in.stl) | No exact 3MF job match; possible same-name print job 3DP-5-101 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-5-103 | [3DP-5-103_Vac-Splitter-for-Silicone-Tubing.3mf](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/01-Vacuum-and-Air-Fittings/3DP-5-103_Vac-Splitter-for-Silicone-Tubing.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-5-104 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-5-104 | [3DP-5-104_Vac-Splitter-for-Silicone-Tubing.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/01-Vacuum-and-Air-Fittings/3DP-5-104_Vac-Splitter-for-Silicone-Tubing.stl) | No exact 3MF job match; possible same-name print job 3DP-5-103 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-5-201 | [3DP-5-201_Nitrogen-Manifold-Holder.3mf](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/02-Gas-Supply-and-Manifolds/3DP-5-201_Nitrogen-Manifold-Holder.3mf) | 1 build item(s); 1 built mesh reference(s); no exact STL match; 1 unmatched; possible same-name STL: 3DP-5-202 | Inspect unmatched/absent print-project geometry; compare same-name mesh (different geometry) |
| 3DP-5-202 | [3DP-5-202_Nitrogen-Manifold-Holder.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/02-Gas-Supply-and-Manifolds/3DP-5-202_Nitrogen-Manifold-Holder.stl) | No exact 3MF job match; possible same-name print job 3DP-5-201 | Compare likely STL/3MF pair; meshes differ despite matching names |
| 3DP-5-301 | [3DP-5-301_Spout-Drain-10x100mm-Linear-Rod-Clamp-2.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-301_Spout-Drain-10x100mm-Linear-Rod-Clamp-2.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-302 | [3DP-5-302_Spout-Drain-10x100mm-Linear-Rod-Clamp-3.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-302_Spout-Drain-10x100mm-Linear-Rod-Clamp-3.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-303 | [3DP-5-303_Spout-Drain-10x100mm-Linear-Rod-Clamp-4.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-303_Spout-Drain-10x100mm-Linear-Rod-Clamp-4.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-304 | [3DP-5-304_Spout-Drain-10x100mm-Linear-Rod-Clamp-5.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-304_Spout-Drain-10x100mm-Linear-Rod-Clamp-5.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-305 | [3DP-5-305_Spout-Drain-Base-Connecting-Rail-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-305_Spout-Drain-Base-Connecting-Rail-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate; same geometry as 3DP-5-306 |
| 3DP-5-306 | [3DP-5-306_Spout-Drain-Base-Connecting-Rail-2.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-306_Spout-Drain-Base-Connecting-Rail-2.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate; same geometry as 3DP-5-305 |
| 3DP-5-307 | [3DP-5-307_Spout-Drain-Base-Cover-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-307_Spout-Drain-Base-Cover-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-308 | [3DP-5-308_Spout-Drain-Clamp-to-Base-Bracket-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-308_Spout-Drain-Clamp-to-Base-Bracket-1.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-309 | [3DP-5-309_Spout-Drain-Clamp-to-Base-Bracket-2.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-309_Spout-Drain-Clamp-to-Base-Bracket-2.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-310 | [3DP-5-310_Spout-Drain-Clamp-to-Base-Bracket-3.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-310_Spout-Drain-Clamp-to-Base-Bracket-3.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-311 | [3DP-5-311_Spout-Drain-Clamp-to-Base-Bracket-4.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-311_Spout-Drain-Clamp-to-Base-Bracket-4.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-312 | [3DP-5-312_Spout-Drain-Complete-Set.3mf](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-312_Spout-Drain-Complete-Set.3mf) | 14 build item(s); 14 built mesh reference(s); STL: 3DP-5-301, 3DP-5-302, 3DP-5-303, 3DP-5-304, 3DP-5-308, 3DP-5-309, 3DP-5-310, 3DP-5-311, 3DP-5-317, 3DP-5-318, 3DP-5-319, 3DP-5-320; 2 unmatched | Inspect unmatched/absent print-project geometry; compare similar-size meshes |
| 3DP-5-313 | [3DP-5-313_Spout-Drain-Copy-of-Spout-Drain-Plate-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-313_Spout-Drain-Copy-of-Spout-Drain-Plate-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-314 | [3DP-5-314_Spout-Drain-Mid-Height-Attachment-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-314_Spout-Drain-Mid-Height-Attachment-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-315 | [3DP-5-315_Spout-Drain-Mid-Height-Attachment-Arms-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-315_Spout-Drain-Mid-Height-Attachment-Arms-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-316 | [3DP-5-316_Spout-Drain-Mid-Height-Attachment-Arms-2.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-316_Spout-Drain-Mid-Height-Attachment-Arms-2.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-317 | [3DP-5-317_Spout-Drain-Mount-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-317_Spout-Drain-Mount-1.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-318 | [3DP-5-318_Spout-Drain-Mount-Bottom-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-318_Spout-Drain-Mount-Bottom-1.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-319 | [3DP-5-319_Spout-Drain-Mount-Bottom-Mirror-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-319_Spout-Drain-Mount-Bottom-Mirror-1.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-320 | [3DP-5-320_Spout-Drain-Mount-Mirrored-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-320_Spout-Drain-Mount-Mirrored-1.stl) | Exact mesh in 3DP-5-312 | Confirm function, design revision and physical compatibility |
| 3DP-5-321 | [3DP-5-321_Spout-Drain-Platform.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-321_Spout-Drain-Platform.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-322 | [3DP-5-322_Spout-Drain-rod-connector-1.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-322_Spout-Drain-rod-connector-1.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-5-323 | [3DP-5-323_Spout-Drain-rod-connector-2.stl](../Rig-Engineering-Files/05-Vacuum-Gas-and-Drainage/3D-Printing/03-Spout-Drain-Assembly/3DP-5-323_Spout-Drain-rod-connector-2.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |

### 07 Experimental Control Sensing and Data

| File ID | Actual file | Geometry-based relationship | Human review needed |
| --- | --- | --- | --- |
| 3DP-7-101 | [3DP-7-101_Signal-Enhancer-Case.stl](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/01-Sensors-and-Signal-Conditioning/3DP-7-101_Signal-Enhancer-Case.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-7-102 | [3DP-7-102_Signal-Enhancer-Cover.stl](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/01-Sensors-and-Signal-Conditioning/3DP-7-102_Signal-Enhancer-Cover.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |
| 3DP-7-201 | [3DP-7-201_Barrier-Strip-Case.stl](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/02-Controllers-and-Wiring/3DP-7-201_Barrier-Strip-Case.stl) | Exact mesh in 3DP-7-202 | Confirm function, design revision and physical compatibility |
| 3DP-7-202 | [3DP-7-202_Barrier-Strip-Case-Both-components-for-ONE.3mf](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/02-Controllers-and-Wiring/3DP-7-202_Barrier-Strip-Case-Both-components-for-ONE.3mf) | 2 build item(s); 2 built mesh reference(s); STL: 3DP-7-201, 3DP-7-203 | Confirm multi-part count, fit and slicer settings |
| 3DP-7-203 | [3DP-7-203_Barrier-Strip-Cover.stl](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/02-Controllers-and-Wiring/3DP-7-203_Barrier-Strip-Cover.stl) | Exact mesh in 3DP-7-202 | Confirm function, design revision and physical compatibility |
| 3DP-7-204 | [3DP-7-204_case-cover.stl](../Rig-Engineering-Files/07-Experimental-Control-Sensing-and-Data/3D-Printing/02-Controllers-and-Wiring/3DP-7-204_case-cover.stl) | No exact 3MF job match | Check whether an existing prepared print job is appropriate |

## Suggested descriptive filenames — not applied

For a 3MF that has been matched to STL meshes, adding a PrintJob- label
can clarify that it is a saved printing project, not an individual part.
Do NOT approve these candidates without checking actual job contents.

| ID | Current 3MF filename | Naming candidate |
| --- | --- | --- |
| 3DP-1-202 | 3DP-1-202_Cage-Alignment-Set.3mf | 3DP-1-202_PrintJob-Cage-Alignment-Set.3mf |
| 3DP-1-307 | 3DP-1-307_Top-Lock-Pivot-Mount.3mf | 3DP-1-307_PrintJob-Top-Lock-Pivot-Mount.3mf |
| 3DP-2-101 | 3DP-2-101_Frame-Tower-Foot.3mf | 3DP-2-101_PrintJob-Frame-Tower-Foot.3mf |
| 3DP-2-301 | 3DP-2-301_Single-Spout-Barrel-PLA.3mf | 3DP-2-301_PrintJob-Single-Spout-Barrel-PLA.3mf |
| 3DP-2-303 | 3DP-2-303_Spout-Spacer-shorter-spout.3mf | 3DP-2-303_PrintJob-Spout-Spacer-shorter-spout.3mf |
| 3DP-2-401 | 3DP-2-401_spout-clamp-to-mount-bracket.3mf | 3DP-2-401_PrintJob-spout-clamp-to-mount-bracket.3mf |
| 3DP-2-501 | 3DP-2-501_Teflon-Tube-Vac-Hole-Tool.3mf | 3DP-2-501_PrintJob-Teflon-Tube-Vac-Hole-Tool.3mf |
| 3DP-3-207 | 3DP-3-207_Stimulus-Frame-Backbone.3mf | 3DP-3-207_PrintJob-Stimulus-Frame-Backbone.3mf |
| 3DP-3-209 | 3DP-3-209_Stimulus-Frame-Backbone-End.3mf | 3DP-3-209_PrintJob-Stimulus-Frame-Backbone-End.3mf |
| 3DP-3-213 | 3DP-3-213_Syringe-Holder.3mf | 3DP-3-213_PrintJob-Syringe-Holder.3mf |
| 3DP-3-215 | 3DP-3-215_Syringe-Holder-Top.3mf | 3DP-3-215_PrintJob-Syringe-Holder-Top.3mf |
| 3DP-7-202 | 3DP-7-202_Barrier-Strip-Case-Both-components-for-ONE.3mf | 3DP-7-202_PrintJob-Barrier-Strip-Case-Both-components-for-ONE.3mf |

## STL files with matching normalized mesh geometry

- 3DP-5-305, 3DP-5-306 (review roles and orientation; NOT automatic duplicates for deletion)

## What will update automatically?

- The file lists, counts, exact geometry associations and candidate-name checks
  rerun whenever the workflow is triggered by relevant committed branch changes.
- The change list reflects the triggering Git push when prior history is available.
- **Physical printing, actual print dates, installed/working status, approvals and
  functional intent cannot be inferred from geometry or Git commits.**
- Mesh matching is sensitive to rotation, tessellation and scale. Some 3MF
  layouts contain composite objects, modifiers or proprietary slicer extensions.
- Other details remain in the downloadable full JSON/CSV workflow artifacts.
