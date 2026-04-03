import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
import os

# Parametri relativi rispetto alla posizione dello script
script_dir = os.path.dirname(os.path.abspath(__file__))
base_root = os.path.dirname(script_dir) # Cartella Tesina Wireshark
csv_path = os.path.join(base_root, "capture.csv")
output_dir = base_root

# Lettura dati
times = []
protocols = []

with open(csv_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            times.append(float(row['Time']))
            protocols.append(row['Protocol'])
        except:
            continue

# 1. Calcolo tempi di interarrivo
inter_arrival_times = [times[i] - times[i-1] for i in range(1, len(times))]

mean_iat = statistics.mean(inter_arrival_times)
median_iat = statistics.median(inter_arrival_times)
stdev_iat = statistics.stdev(inter_arrival_times)

# 2. Conteggio protocolli
proto_counts = {}
for p in protocols:
    proto_counts[p] = proto_counts.get(p, 0) + 1

# Ordinamento per visualizzazione migliore
sorted_protos = dict(sorted(proto_counts.items(), key=lambda item: item[1], reverse=True))

# 3. Generazione Grafico Frequenza Cumulativa (CDF)
sorted_iat = np.sort(inter_arrival_times)
y_values = np.arange(len(sorted_iat)) / float(len(sorted_iat) - 1)

plt.figure(figsize=(10, 6))
plt.plot(sorted_iat, y_values, marker='.', linestyle='none', color='#2c3e50')
plt.title('Frequenza Cumulativa (CDF) dei Tempi di Interarrivo', fontsize=14, fontweight='bold')
plt.xlabel('Tempo di Interarrivo (s)', fontsize=12)
plt.ylabel('Probabilità Cumulativa', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, 'cdf_interarrival.png'), dpi=300, bbox_inches='tight')
plt.close()

# 4. Generazione Istogramma Protocolli
plt.figure(figsize=(10, 6))
plt.bar(sorted_protos.keys(), sorted_protos.values(), color='#3498db', edgecolor='#2980b9')
plt.title('Distribuzione dei Protocolli (Istogramma)', fontsize=14, fontweight='bold')
plt.xlabel('Protocollo', fontsize=12)
plt.ylabel('Numero di Pacchetti', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, 'protocol_histogram.png'), dpi=300, bbox_inches='tight')
plt.close()

# 5. Generazione Grafico a Torta Protocolli
plt.figure(figsize=(8, 8))
# Raggruppo i protocolli minori in "Others" se sono troppi (> 6)
if len(sorted_protos) > 6:
    top_protos = list(sorted_protos.items())[:5]
    others_count = sum(count for label, count in list(sorted_protos.items())[5:])
    pie_data = dict(top_protos)
    pie_data['Others'] = others_count
else:
    pie_data = sorted_protos

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4fb6d']
plt.pie(pie_data.values(), labels=pie_data.keys(), autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'white'})
plt.title('Distribuzione Percentuale dei Protocolli', fontsize=14, fontweight='bold')
plt.savefig(os.path.join(output_dir, 'protocol_pie.png'), dpi=300, bbox_inches='tight')
plt.close()

# Stampa dei risultati
print(f"MEAN_IAT: {mean_iat:.6f}")
print(f"MEDIAN_IAT: {median_iat:.6f}")
print(f"STDEV_IAT: {stdev_iat:.6f}")
print("PROTOCOLS:")
for k, v in sorted_protos.items():
    print(f"{k}: {v}")
