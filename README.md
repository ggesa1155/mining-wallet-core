# Dust Sweeper

**Dust Sweeper** — инструмент для поиска и анализа "пылевых" (dust) выходов (UTXO) на Bitcoin-адресе.

## Зачем нужен

"Пыль" — это выходы с очень малой суммой (обычно < 546 сатоши), которые невыгодно тратить из-за комиссии. Этот инструмент находит такие UTXO, чтобы помочь:
- провести консолидацию,
- понять, откуда пыль,
- предотвратить анализ или слежку.

## Использование

```bash
python dust_sweeper.py <your-bitcoin-address>
```

## Установка

```bash
pip install -r requirements.txt
```

## Пример

```bash
python dust_sweeper.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
```

## Лицензия

MIT
