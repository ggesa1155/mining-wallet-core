"""
Dust Sweeper — утилита для анализа "пылевых" UTXO и подготовки к их очистке.
"""

import requests
import argparse

DUST_LIMIT = 546  # сатоши

def get_utxos(address):
    url = f"https://blockstream.info/api/address/{address}/utxo"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("❌ Ошибка получения данных от Blockstream API.")
    return r.json()

def sweep_dust(address):
    utxos = get_utxos(address)
    dust_utxos = [u for u in utxos if u['value'] <= DUST_LIMIT]
    print(f"📬 Адрес: {address}")
    print(f"🔎 Найдено UTXO: {len(utxos)} | Пылевых (≤{DUST_LIMIT} сат): {len(dust_utxos)}")
    total_dust = sum(u['value'] for u in dust_utxos)
    print(f"💸 Суммарная пыль: {total_dust} сатоши")
    print("\n📋 Подробности:")
    for i, u in enumerate(dust_utxos, 1):
        print(f"{i}. TXID: {u['txid']} | Index: {u['vout']} | Сумма: {u['value']} сатоши")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dust Sweeper — поиск и анализ пыльных UTXO.")
    parser.add_argument("address", help="Bitcoin-адрес")
    args = parser.parse_args()
    sweep_dust(args.address)
