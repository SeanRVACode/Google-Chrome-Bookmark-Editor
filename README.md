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

1. Download the exe from emailed link.
2. Run the executable file `Chrome Tax Payment Bookmark Creator.exe`

## Usage

**Important:** Before running this tool:

1. Make sure Google Chrome is completely closed (check Task Manager to ensure no Chrome processes are running)
2. Run the program once - it will create a backup of your bookmarks
3. It will prompt you to choose a bookmarks path. You will want to select the one that has `Chrome\<various letters>\Default\Bookmarks`
4. Open Chrome and verify the new bookmarks have been added correctly

## ⚠️ Warnings

- **ALWAYS ENSURE CHROME IS CLOSED** before running this tool to avoid data corruption
- The program automatically creates a backup of your Chrome bookmarks file (with a `.bak` extension) the first time it runs
- Currently configured for the default Chrome profile location. Users with custom Chrome installations or multiple profiles may need to adjust the path in the source code
- This tool directly modifies Chrome's bookmarks file, use with caution

## Technical Details

- Written in Python
- Manipulates Chrome's `Bookmarks` JSON file directly
- The bookmark path most likely to work in office is: `%LOCALAPPDATA%\Google\Chrome\<various letters>\Default\Bookmarks`
  - `<various letters>` usually contains an \_ in the string.
  - If your Chrome installation uses a different path, you'll need to make sure to select the correct path.

## Troubleshooting

- If bookmarks don't appear, verify that Chrome is using the default profile location
- If Chrome displays an error about corrupted bookmarks:
  1. Close Chrome
  2. Locate the backup file created at `%LOCALAPPDATA%\Google\Chrome\<user unique installation folder naming>\Default\Bookmarks.bak`
  3. Copy this file to `%LOCALAPPDATA%\Google\Chrome\<user unique installtion folder naming>\Default\Bookmarks`
  4. Restart Chrome

## License

This project is provided for personal and business use as-is with no warranty.
