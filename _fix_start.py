from pathlib import Path
p = Path("network/server.py")
c = p.read_text(encoding="utf-8")

if "\napp = create_app(" not in c and "# FAABLE-FALLBACK" not in c:
    fallback = '''

# FAABLE-FALLBACK: если запускают network.server:app — создаём app из env
import os as _os
if _os.environ.get("PORT"):
    _port = int(_os.environ["PORT"])
    _data_dir = Path("data")
    app = create_app(
        port=_port,
        data_file=str(_data_dir / "chain_A.json"),
        self_url=f"http://0.0.0.0:{_port}",
        peers_file=str(_data_dir / f"peers_{_port}.json"),
        gifts_file=str(_data_dir / f"gifts_{_port}.json"),
        timelocks_file=str(_data_dir / f"timelocks_{_port}.json"),
        sbt_file=str(_data_dir / f"sbt_{_port}.json"),
        inheritance_file=str(_data_dir / f"inheritance_{_port}.json"),
        id_file=str(_data_dir / f"ids_{_port}.json"),
        burn_file=str(_data_dir / f"burn_{_port}.json"),
        contacts_file=str(_data_dir / f"contacts_{_port}.json"),
        swap_file=str(_data_dir / f"swap_{_port}.json"),
        poc_file=str(_data_dir / f"poc_{_port}.json"),
        p2p_file=str(_data_dir / f"p2p_{_port}.json"),
    )
'''
    c = c.rstrip() + fallback
    p.write_text(c, encoding="utf-8")
    print("OK: fallback app добавлен в server.py")
else:
    print("ℹ️ app уже есть или fallback уже стоит")
