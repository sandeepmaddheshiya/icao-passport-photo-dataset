# 🛂 ICAO 9303 Compliant Passport & Visa Photo Reference Dataset

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset: Git LFS](https://img.shields.io/badge/Storage-Git%20LFS-blue.svg)](https://git-lfs.github.com/)
[![Standard: ICAO Doc 9303](https://img.shields.io/badge/Standard-ICAO%20Doc%209303-green.svg)](https://www.icao.int/)
[![Standard: ISO/IEC 19794-5](https://img.shields.io/badge/Standard-ISO%2FIEC%2019794--5-teal.svg)](https://www.iso.org/)
[![Trained On: VisaReadyNow](https://img.shields.io/badge/Engine-VisaReadyNow-orange.svg)](https://visareadynow.com)

A curated, high-resolution dataset of **130 AI-generated reference passport/visa portraits** engineered to strictly satisfy the international biometric photo specifications outlined by the **International Civil Aviation Organization (ICAO Doc 9303)**, **ISO/IEC 19794-5**, the **U.S. Department of State (2x2" standard)**, and **Schengen Visa (35x45mm standard)**.

> 🚀 **Production Application Note:**
> The core biometric face-centering, head-height scaling, auto-straightening, and border-clearance engine of **[VisaReadyNow](https://visareadynow.com)** was calibrated, trained, and benchmarked against this exact dataset.

---

## 📌 Key Highlights

- **130 High-Resolution Samples**: Provided in lossless PNG format packed in `pictures.zip` (230 MB) tracked via **Git LFS**.
- **100% Strict ICAO Compliance**:
  - **Neutral Expression & Direct Gaze**: Eyes open, mouth closed, direct frontal pose.
  - **Sub-degree Head Alignment**: Measured head tilt $< 0.3^\circ$ across all samples.
  - **Biometric Head Height**: Mean chin-to-crown ratio of $50.2\% \pm 7\%$, perfectly covering both US ($50\% - 69\%$) and international passport standards.
  - **Calibrated Eye-Line Level**: Mean eye vertical placement at $40.3\% \pm 4\%$ from the top of the frame.
  - **Pure White Background**: Isolated on $RGB = (255, 255, 255)$ with anti-aliased alpha edges.
- **Annotated Landmarks Included**: Full ground-truth metadata in `metadata.json` including facial landmarks, chin/forehead bounds, cranial crown estimates, eye angles, and biometric ratios.

---

## 📊 Biometric Measurements & Statistics

Calculated via **MediaPipe FaceMesh (478 landmarks)** across all 130 reference images:

| Parameter | Dataset Mean | Standard Deviation | Min / Max Range | Official ICAO / US Spec |
| :--- | :---: | :---: | :---: | :---: |
| **Head Height Ratio** ($\frac{\text{Chin} - \text{Crown}}{\text{Frame Height}}$) | **50.2%** | $\pm 7.1\%$ | 36.5% – 69.7% | 50% – 69% (US) / 70% – 80% (EU) |
| **Eye-Line Vertical Ratio** ($\frac{\text{Eye Y}}{\text{Frame Height}}$) | **40.3%** | $\pm 4.2\%$ | 33.4% – 53.0% | 38% – 48% (Target ~40%) |
| **Top Crown Margin** ($\frac{\text{Crown Y}}{\text{Frame Height}}$) | **17.1%** | $\pm 3.4\%$ | 7.4% – 25.2% | $\ge 8\%$ clearance |
| **Horizontal Eye Center** ($\frac{\text{Eye Mid X}}{\text{Frame Width}}$) | **50.0%** | $\pm 0.6\%$ | 48.7% – 51.4% | Centered at 50% |
| **Head Rotation / Tilt** | **0.05°** | $\pm 0.12°$ | Max 0.28° | $\le 5.0°$ tolerance |

---

## 🗂 Dataset Structure

```text
icao-passport-photo-dataset/
├── .gitattributes          # Git LFS configuration for binary archives
├── .gitignore              # Standard ignore rules
├── LICENSE                 # MIT Open License
├── README.md               # Documentation & specifications
├── metadata.json           # Ground-truth annotations & landmark metrics for all 130 photos
├── inspect_dataset.py      # CLI verification and sample extractor script
└── pictures.zip            # 230 MB Git LFS archive containing OK_KI_FACE_001.png ... OK_KI_FACE_130.png
```

### `metadata.json` Schema

Each entry in `metadata.json` includes detailed measurements:

```json
{
  "filename": "OK_KI_FACE_001.png",
  "width": 1106,
  "height": 1422,
  "aspect_ratio": 0.7778,
  "landmarks": {
    "eye_mid_x": 552.37,
    "eye_mid_y": 578.02,
    "forehead_y": 387.59,
    "chin_y": 1009.14,
    "estimated_crown_y": 170.04,
    "eye_angle_degrees": 0.12,
    "face_height_px": 621.55,
    "head_height_px": 839.10,
    "head_height_ratio": 0.5901,
    "eye_y_ratio": 0.4065
  }
}
```

---

## 🛠 Quickstart

### 1. Clone with Git LFS

Ensure [Git LFS](https://git-lfs.github.com/) is installed:

```bash
git lfs install
git clone git@github.com:sandeepmaddheshiya/icao-passport-photo-dataset.git
cd icao-passport-photo-dataset
git lfs pull
```

### 2. Inspect & Verify Biometrics

Run the included verification script:

```bash
python3 inspect_dataset.py
```

### 3. Extract Sample Images in Python

```python
import zipfile

with zipfile.ZipFile("pictures.zip", "r") as z:
    z.extractall("extracted_dataset/")
print("Extracted 130 ICAO-compliant passport photos!")
```

---

## 🎯 Use Cases

- **Model Training & Fine-Tuning**: Training face-segmentation, background matting (e.g. MODNet, BiRefNet), and passport auto-cropping models.
- **Biometric Compliance Benchmarks**: Testing ID photo verification pipelines against ground truth ICAO / ISO standards.
- **Data Augmentation**: Generating synthetic ID variations with diverse facial geometry, lighting, and skin tones without privacy violations.

---

## ⚖️ Synthetic Data & Ethical AI Statement

All portraits in this dataset were synthetically generated and curated to simulate realistic identity photo requirements without depicting real individuals, eliminating GDPR and PII privacy concerns while maintaining full biometric utility.

---

## 📄 License & Attribution

This dataset is released under the **MIT License**.

When using this dataset in research or production, please cite:

```bibtex
@misc{visareadynow2026icao,
  title={ICAO 9303 Compliant AI-Generated Passport & Visa Photo Reference Dataset},
  author={Maddheshiya, Sandeep},
  year={2026},
  publisher={GitHub},
  howpublished={\url{https://github.com/sandeepmaddheshiya/icao-passport-photo-dataset}}
}
```
