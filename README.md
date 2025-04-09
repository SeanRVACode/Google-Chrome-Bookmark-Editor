# Google Chrome Bookmark Editor - Tax Payment Links

A utility tool that automatically adds a collection of tax payment bookmarks to Google Chrome.

## Description

This tool creates a new folder called "Tax Payments" in your Google Chrome bookmarks bar and populates it with direct links to various tax payment portals including IRS and Virginia state tax payment websites. It's particularly useful for accounting professionals or businesses that need quick access to tax payment sites.

## Features

- Creates a "Tax Payments" folder in your Chrome bookmarks bar
- Adds 9 pre-configured tax payment bookmarks:
  - IRS Business Payment
  - VA Corporate Extension
  - VA Corporate Balance Due
  - VA Corporate Estimated Tax
  - VA PTET Payment
  - IRS Individual Payment
  - VA Individual Extension Payment
  - VA Individual Balance Due
  - VA Individual Estimated Tax
- Automatically backs up your existing bookmarks file before making changes

## Installation

1. Download the latest release from the releases section
2. Extract the ZIP file to a location of your choice
3. Run the executable file `Chrome Tax Payment Bookmark Creator.exe`

## Usage

**Important:** Before running this tool:

1. Make sure Google Chrome is completely closed (check Task Manager to ensure no Chrome processes are running)
2. Run the program once - it will create a backup of your bookmarks and add the tax payment folder
3. Open Chrome and verify the new bookmarks have been added correctly

## ⚠️ Warnings

- **ALWAYS ENSURE CHROME IS CLOSED** before running this tool to avoid data corruption
- The program automatically creates a backup of your Chrome bookmarks file (with a `.bak` extension) the first time it runs
- Currently configured for the default Chrome profile location. Users with custom Chrome installations or multiple profiles may need to adjust the path in the source code
- This tool directly modifies Chrome's bookmarks file, use with caution

## Technical Details

- Written in Python
- Manipulates Chrome's `Bookmarks` JSON file directly
- The bookmark path is set to: `%LOCALAPPDATA%\Google\Chrome\d_vfedpxi\Default\Bookmarks`
  - If your Chrome installation uses a different path, you'll need to modify the source code

## Troubleshooting

- If bookmarks don't appear, verify that Chrome is using the default profile location
- If Chrome displays an error about corrupted bookmarks:
  1. Close Chrome
  2. Locate the backup file created at `%LOCALAPPDATA%\Google\Chrome\d_vfedpxi\Default\Bookmarks.bak`
  3. Copy this file to `%LOCALAPPDATA%\Google\Chrome\d_vfedpxi\Default\Bookmarks`
  4. Restart Chrome

## License

This project is provided for personal and business use as-is with no warranty.

## Contributing

Contributions welcome! Feel free to fork this repository and submit pull requests.
