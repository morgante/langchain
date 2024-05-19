# Testing the replace_imports migration

This runs the v0.2 migration with a desired set of rules.

```grit
migrate:
  version: 0.2
  rules:
    - replace_imports:
        - from: "old_module"
          to: "new_module"
```

## Single import

Before:

```python
from langchain.chat_models import ChatOpenAI
```

After:

```python
from langchain_community.chat_models import ChatOpenAI
```

## Community to partner

```python
from langchain_community.chat_models import ChatOpenAI
```

```python
from langchain_openai import ChatOpenAI
```

## Noop

```python
from foo import ChatOpenAI
```

```python
from foo import ChatOpenAI
```

## Mixed imports

```python
from langchain_community.chat_models import ChatOpenAI, ChatAnthropic, foo
```

```python
from langchain_community.chat_models import foo
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
```
