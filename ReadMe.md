# AFK

Travis L. Seymour, PhD

A command-line utility that periodically moves the mouse to prevent your screen from sleeping or timing out. Useful when you don't have admin access to install other keep-awake utilities. Works on macOS and Linux.

> NOTE: This was script was coded for my personal use in a single context when giving exams on campus, when the available iMac has limited tools and restrictive permissions. In most cases, systems have a way to keep the session alive without this software. I consider this a throwaway tool and I do not plan to update or extend it with other functionality; thus use it as your own risk. If you do plan to use it, read main.py -- it's pretty simple.

---

## Requirements

- Python 3.11 or later
- macOS: You may need to grant accessibility permissions to your terminal when first running the tool. In the one context where I needed this tool, I did not have to grant such permissions. YMMV.

## Installing uv

If you don't already have `uv` installed, you can install it with:

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For other installation methods, see the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/).

## Installing AFK

```bash
uv tool install git+https://github.com/travisseymour/afk
```

## Usage

Run with default settings (moves mouse 5 pixels every 15 seconds):

```bash
afk
```

Press `Ctrl+C` to stop.

### Other Parameters

Customize the interval (in seconds):

```bash
afk --interval 30  # default 15
```

Customize the number of pixels to move:

```bash
afk --pixels 3  # default 5
```

Combine options:

```bash
afk -i 60 -p 10
```

View help:

```bash
afk --help
```

## Uninstalling AFK

```bash
uv tool uninstall afk
```

