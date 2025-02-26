# An Automated High-Throughput Lighting System for Screening Photosynthetic Microorganisms in Plate-Based Formats

## Authors
Avery J. C. Noonan<sup>1,4,7</sup>, Paula M. N. Cameron<sup>2,4</sup>, Kalen Dofher<sup>2,4</sup>, Nannaphat Sukkasam<sup>2,4,5</sup>, Tony Liu<sup>3,4</sup>, Lucas Rönn<sup>2</sup>, Tanakarn Monshupanee<sup>5</sup>, and Steven J. Hallam<sup>1,2,3,4,6,7*</sup>

## Abstract
The capacity of photosynthetic microorganisms to fix carbon dioxide into biomass positions them as promising cell factories for industrial bioproduction with reduced environmental impact. However, limitations in screening throughput hinder the identification of enzymes, strains, and growth conditions needed to realize this potential. Here we present a microplate-based high-throughput cultivation system that can be integrated into existing automation infrastructure and supports growth of both prokaryotic and eukaryotic photosynthetic microorganisms. In one application, we optimize BG-11 medium compositions for *Synechococcus elongatus* UTEX 2973, *Chlamydomonas reinhardtii* UTEX 90, and *Nostoc hatei* CUBC1040, resulting in growth rate increases of 38.4% to 61.6%. In another application, we identify small molecules that influence growth rates in *Synechococcus elongatus* UTEX 2973, including candidate compounds for growth rate increase and dozens that prevent growth. The sensitivity, throughput, and extensibility of this system support screening, strain isolation, and growth optimization needed for the development of photosynthetic microbial cell factories.

---

## Repository Contents
The following table shows the contents of the repository and a brief description of each file:

| File | Topic | Directory | Description |
|------|-------|-----------|-------------|
| **Noonan_HTP_lighting_system_figures.Rmd** | RMarkdown | . | RMarkdown generating all data figures |
| **Noonan_BG11-RSM_JMP_data_processing.Rmd** | RMarkdown | . | RMarkdown for RSM data reformatting for input into JMP |
| **PHERAstar_2x2_data_processing.py** | Python | . | Script for processing PHERAstar 2x2 data |
| **PHERAstar_standard_data_processing.py** | Python | . | Script for processing standard PHERAstar data |
| **varioskan_data_parsing.py** | Python | . | Script for parsing Varioskan data |
| **LED_driver.ino** | Arduino | . | Arduino script for controlling LED intensity |
| **parts-list.csv** | System | system-design/ | Parts list |
| **2973_plate-type_growth_data.csv** | Design / Validation | data/system-design/ | Culture OD data |
| **2973_seal_growth_data.csv** | Design / Validation | data/system-design/ | Culture OD data |
| **2973_spectrum_growth_data.csv** | Design / Validation | data/system-design/ | Culture OD data |
| **photodiode_array_data.csv** | Design / Validation | data/system-design/ | Photodiode data |
| **sensor_array_data.csv** | Design / Validation | data/system-design/ | Photodiode data |
| **layout_info.csv** | Design / Validation | data/system-design/ | Plate layout info |
| **echo_evaporation_data.csv** | Design / Validation | data/system-design/ | Evaporation data |
| **2973_BG11_growth_data.csv** | Primary Use-Cases | data/use-cases/primary/ | Culture OD data |
| **2973_BG11_plate_layout.csv** | Primary Use-Cases | data/use-cases/primary/ | Plate layout info |
| **2973_BG11_plate_metadata.csv** | Primary Use-Cases | data/use-cases/primary/ | Culture metadata |
| **antibiotics_growth_data.csv** | Primary Use-Cases | data/use-cases/primary/ | Culture OD data |
| **antiobiotics_plate_layout.csv** | Primary Use-Cases | data/use-cases/primary/ | Plate layout info |
| **antiobiotics_plate_metadata.csv** | Primary Use-Cases | data/use-cases/primary/ | Culture metadata |
| **layout_info.csv** | Primary Use-Cases | data/use-cases/primary/ | Plate layout info |
| **BG11_JMP_layout.csv** | BG-11 RSM | data/use-cases/BG11-RSM/ | Plate layout info |
| **BG11_opt_OD_data.csv** | BG-11 RSM | data/use-cases/BG11-RSM/ | Culture OD data |
| **flask_biomass_data_100uM.csv** | BG-11 RSM | data/use-cases/BG11-RSM/ | Culture biomass data |
| **bioactive_library_info.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Screening library information |
| **bioactive_screen1_OD_data.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Culture OD data |
| **bioactive_round2_OD_data.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Culture OD data |
| **bioactive_screen_round2_hit_compound_info.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Compound metadata |
| **bioactive_screen_round3_layout.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Plate layout info |
| **bioactive_screen_round3_OD_data.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Culture OD data |
| **bioactive_gradient_data.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Culture OD data |
| **gossypetin_scan_data.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Culture OD data |
| **layout_info.csv** | Bioactive Screen | data/use-cases/bioactive-screening/ | Plate layout info |
| **slipring_connector.stl** | Design / Validation | 3D model (.stl) | Model of slipring connector |
| **LED_array_support.stl** | Design / Validation | 3D model (.stl) | Model of LED array support structure |

---

## How to Cite
Please cite this repository and associated publication as follows:
> Noonan, A.J.C., Cameron, P.M.N., Dofher, K., Sukkasam, N., Liu, T., Rönn, L., Monshupanee, T., and Hallam, S.J. (2025). An automated high-throughput lighting system for screening photosynthetic microorganisms in plate-based formats.

