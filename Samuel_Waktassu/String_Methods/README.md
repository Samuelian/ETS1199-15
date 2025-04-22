# truncate_string()

Shortens a string to a specified length and adds a suffix if truncated.

## Features
- Adds a custom suffix like "..." if string is too long
- Prevents mid-word truncation if desired (basic version)

## Example

```python
from custom_string_methods import truncate_string

print(truncate_string("This is a very long sentence that needs trimming.", 20))
# Output: "This is a very lo..."
