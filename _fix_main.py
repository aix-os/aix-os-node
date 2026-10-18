from pathlib import Path
p = Path("main.py")
c = p.read_text(encoding="utf-8")
if "p2p_file" not in c:
    c = c.replace(
        '    poc_file="data/poc_8010.json",',
        '    poc_file="data/poc_8010.json",\n    p2p_file="data/p2p_8010.json",',
    )
    p.write_text(c, encoding="utf-8")
    print("OK: main.py — p2p_file добавлен")
else:
    print("ℹ️ p2p_file уже есть")
