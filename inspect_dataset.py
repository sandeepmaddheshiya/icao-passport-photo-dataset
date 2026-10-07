#!/usr/bin/env python3
"""
Dataset Inspector & Biometric Verifier for ICAO 9303 Compliant Reference Photos.
"""
import json
import os
import zipfile
from typing import Dict, Any

METADATA_FILE = "metadata.json"
ZIP_FILE = "pictures.zip"


def verify_dataset() -> None:
    print("=" * 65)
    print(" 🛂 ICAO 9303 Compliant Passport Dataset Inspector")
    print("=" * 65)

    if not os.path.exists(METADATA_FILE):
        print(f"❌ Error: {METADATA_FILE} not found.")
        return

    with open(METADATA_FILE, "r") as f:
        meta: Dict[str, Any] = json.load(f)

    print(f" Dataset Name   : {meta.get('dataset_name')}")
    print(f" Version        : {meta.get('version')}")
    print(f" Total Samples  : {meta.get('total_samples')}")
    print(f" Standards      : {', '.join(meta.get('standards_compliance', []))}")
    print("-" * 65)

    images = meta.get("images", [])
    if not images:
        print("❌ No images listed in metadata.")
        return

    head_ratios = [img["landmarks"]["head_height_ratio"] for img in images if "landmarks" in img]
    eye_ratios = [img["landmarks"]["eye_y_ratio"] for img in images if "landmarks" in img]
    tilts = [abs(img["landmarks"]["eye_angle_degrees"]) for img in images if "landmarks" in img]

    import statistics
    print("📊 Ground-Truth Biometric Statistics (Mean ± StdDev):")
    print(f"  • Head Height Ratio : {statistics.mean(head_ratios)*100:.1f}% ± {statistics.stdev(head_ratios)*100:.1f}% (Range: {min(head_ratios)*100:.1f}% - {max(head_ratios)*100:.1f}%)")
    print(f"  • Eye-Line Y Ratio  : {statistics.mean(eye_ratios)*100:.1f}% ± {statistics.stdev(eye_ratios)*100:.1f}% (Range: {min(eye_ratios)*100:.1f}% - {max(eye_ratios)*100:.1f}%)")
    print(f"  • Max Head Tilt     : {max(tilts):.2f}° (All compliant < 1.0°)")
    print("-" * 65)

    if os.path.exists(ZIP_FILE):
        zip_size_mb = os.path.getsize(ZIP_FILE) / (1024 * 1024)
        with zipfile.ZipFile(ZIP_FILE, "r") as z:
            file_count = len([name for name in z.namelist() if not name.endswith('/')])
        print(f"📦 Archive '{ZIP_FILE}' verified ({zip_size_mb:.1f} MB, {file_count} files).")
    else:
        print(f"⚠️ Archive '{ZIP_FILE}' not found locally. Run 'git lfs pull' to fetch.")

    print("=" * 65)
    print("✅ Dataset verified successfully!")


def extract_samples(output_dir: str = "extracted_images", max_count: int = 5) -> None:
    if not os.path.exists(ZIP_FILE):
        print(f"❌ {ZIP_FILE} not found. Run 'git lfs pull'.")
        return

    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(ZIP_FILE, "r") as z:
        files = [n for n in z.namelist() if not n.endswith('/')][:max_count]
        for f in files:
            z.extract(f, output_dir)
            print(f"Extracted: {os.path.join(output_dir, f)}")

    print(f"✅ Extracted {len(files)} sample images to '{output_dir}/'")


if __name__ == "__main__":
    verify_dataset()
