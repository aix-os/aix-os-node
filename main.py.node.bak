import os
from network.server import create_app

# Faable подставляет порт в переменную окружения PORT
PORT = int(os.environ.get("PORT", 8010))
DATA_FILE = "data/chain_A.json"

# Создаем приложение со всеми нужными параметрами
app = create_app(
    port=PORT,
    data_file=DATA_FILE,
    self_url=f"http://0.0.0.0:{PORT}",
    peers_file="data/peers_8010.json",
    gifts_file="data/gifts_8010.json",
    timelocks_file="data/timelocks_8010.json",
    sbt_file="data/sbt_8010.json",
    inheritance_file="data/inheritance_8010.json",
    id_file="data/ids_8010.json",
    burn_file="data/burn_8010.json",
    contacts_file="data/contacts_8010.json",
    swap_file="data/swap_8010.json",
    poc_file="data/poc_8010.json",
)
