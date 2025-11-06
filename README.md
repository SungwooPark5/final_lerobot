## 프로젝트 시작하기

1. 파이썬 가상 환경 `.venv` 설치

```bash
$ python3 -m venv .venv
```

2. 파이썬 가상 환경 실행

```bash
// Linux
$ source .venv/bin/activate

// Window
$ .venv/Scripts/activate.bat
```

3. 파이썬 패키지 관리 `uv` 설치

```bash
$ pip install uv
```

4. 패키지 동기화

```bash
$ uv sync
```
