## 🔹 4. `truncate_string(text, limit, suffix='...')`

### **Python Code:**
```python
def truncate_string(text: str, limit: int, suffix: str = '...') -> str:
    return text if len(text) <= limit else text[:limit - len(suffix)] + suffix
