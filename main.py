import json
import os
from datetime import datetime, timezone
import sys

# Path to chrome bookmarks file (adjust for user or profile if needed)
# bookmarks_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\d_vfedpxi\Default\Bookmarks")

# Define folder and bookmarks
new_folder_name = "Tax Payments"
bookmarks_to_add = [
    {"name": "IRS Business Payment", "url": "https://directpay.irs.gov/directpay/businesspayment?execution=e1s1"},
    {"name": "VA Corporate Extension", "url": "https://www.business.tax.virginia.gov/tax-eforms/500cp.php#"},
    {"name": "VA Corporate Balance Due", "url": "https://www.business.tax.virginia.gov/tax-eforms/500v.php#"},
    {"name": "VA Corporate Estimated Tax", "url": "https://www.business.tax.virginia.gov/tax-eforms/500es.php#"},
    {"name": "VA PTET Payment", "url": "https://www.business.tax.virginia.gov/tax-eforms/ptetpmt.php#"},
    {"name": "IRS Individual Payment", "url": "https://directpay.irs.gov/directpay/payment?execution=e1s1"},
    {"name": "VA Individual Extension Payment", "url": "https://www.business.tax.virginia.gov/tax-eforms/760ip.php"},
    {"name": "VA Individual Balance Due", "url": "https://www.business.tax.virginia.gov/tax-eforms/760pmt.php#"},
    {"name": "VA Individual Estimated Tax", "url": "https://www.business.tax.virginia.gov/tax-eforms/760es.php#"},
]


def select_bookmarks_file(paths):
    print("\nMultiple Chrome profiles found. Select one:")
    for idx, path in enumerate(paths):
        print(f"{idx + 1}: {path}")
    choice = input("Enter number (1-n): ")
    try:
        return paths[int(choice) - 1]
    except (ValueError, IndexError):
        sys.exit("Invalid selection.")


def find_bookmarks_file():
    base_dir = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome")
    bookmark_paths = []

    # Scan all folders in the chrome directory
    for entry in os.listdir(base_dir):
        full_path = os.path.join(base_dir, entry, "Default", "Bookmarks")
        if os.path.isfile(full_path):
            bookmark_paths.append(full_path)

    if not bookmark_paths:
        raise FileNotFoundError("No Chrome bookmarks file found in any profile")

    print("Found the following bookmarks file(s):")
    for path in bookmark_paths:
        print(" -", path)

    return bookmark_paths


bookmarks_paths = find_bookmarks_file()
bookmarks_path = select_bookmarks_file(bookmarks_paths)


def get_timestamp():
    """Generate a timestamp in Chrome's format (microseconds since unix epoch as string)."""
    now = datetime.now(timezone.utc)
    return str(int(now.timestamp() * 1_000_000))


def load_bookmarks(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_bookmarks(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error while saving bookmarks: {e}")
        raise


def add_bookmark_folder(data, folder_name, bookmarks):
    # Get the root "bookmark_bar"
    bookmark_bar = data["roots"]["bookmark_bar"]

    # Create new folder entry
    folder_id = get_timestamp()
    new_folder = {
        "date_added": get_timestamp(),
        "id": folder_id,
        "name": folder_name,
        "type": "folder",
        "children": [],
    }

    # Add each bookmark to the folder
    for bm in bookmarks:
        bm_id = get_timestamp()
        new_folder["children"].append(
            {"date_added": get_timestamp(), "id": bm_id, "name": bm["name"], "type": "url", "url": bm["url"]}
        )

    # Add the folder to the bookmark bar
    bookmark_bar.setdefault("children", []).append(new_folder)
    return data


# Back up original file
backup_path = bookmarks_path + ".bak"
if not os.path.exists(backup_path):
    import shutil

    shutil.copy2(bookmarks_path, backup_path)
    print(f"Backup saved to {backup_path}")


# Load, update, and save
bookmarks_data = load_bookmarks(bookmarks_path)
updated_data = add_bookmark_folder(bookmarks_data, new_folder_name, bookmarks_to_add)
save_bookmarks(bookmarks_path, updated_data)
