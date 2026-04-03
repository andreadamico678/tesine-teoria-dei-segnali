## 1. Operatori e Simboli Matematici Generali

- $\triangleq$ : Definito come (es. $X_k \triangleq A_k e^{j\vartheta_k}$).
- $\Leftrightarrow$ : Coppia trasformata/antitrasformata di Fourier (Dominio del Tempo $\Leftrightarrow$ Dominio della Frequenza).
- $\otimes$ : Operatore di Convoluzione (es. $y(t) = x(t) \otimes h(t)$). _Nota: le slide non usano il classico asterisco $_$, che viene invece usato per il complesso coniugato.\*
- $X^*(f)$ : Complesso coniugato di $X(f)$.
- $|X(f)|$ : Spettro di ampiezza (modulo).
- $\angle X(f)$ oppure $\theta(f)$ o $\vartheta(f)$ : Spettro di fase.
- $\Re\{\cdot\}$ e $\Im\{\cdot\}$ : Parte reale e parte immaginaria.

## 2. Segnali e Funzioni Elementari

- **Gradino unitario:** $u(t)$ (vale 1 per $t>0$, 0 per $t<0$).
- **Impulso di Dirac:** $\delta(t)$ (con la proprietà $\int \delta(t)dt = 1$).
- **Funzione Rettangolare:** $\text{rect}(t/T)$
  - Centrata in $0$, ampiezza $1$, larghezza totale $T$ (estesa da $-T/2$ a $T/2$).
- **Funzione Sinc (Normalizzata):** $\text{sinc}(x) \triangleq \frac{\sin(\pi x)}{\pi x}$
  - _Assunzione fondamentale:_ l'argomento del seno ha il $\pi$. Quindi $\text{sinc}(0) = 1$ e gli zeri si trovano per $x = \pm 1, \pm 2, \dots$
- **Funzione Triangolare:** $\Delta(t/T)$
  - Centrata in $0$, ampiezza $1$ in $0$, si annulla in $-T$ e $+T$ (base totale $2T$).

## 3. Analisi di Fourier e Variabili

- **Variabile di frequenza:** Viene usata **sempre** la frequenza lineare $f$ (in Hz) e quasi mai la pulsazione $\omega$ (in rad/s).
  - _Esponente standard:_ $e^{j2\pi ft}$ (e mai $e^{j\omega t}$). Questo evita di dover inserire i fattori $1/2\pi$ davanti agli integrali.
- **Serie di Fourier (Forma Complessa):**
  - $x(t) = \sum_{k=-\infty}^{+\infty} X_k e^{j2\pi k f_0 t}$
  - Coefficienti: $X_k = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} x(t) e^{-j2\pi k f_0 t} dt$
- **Serie di Fourier (Forma Polare Reale):**
  - $x(t) = A_0 + 2 \sum_{k=1}^{+\infty} A_k \cos(2\pi k f_0 t + \vartheta_k)$
  - _Attenzione:_ Il fattore $2$ è esplicito davanti alla sommatoria. $X_k \triangleq A_k e^{j\vartheta_k}$.
- **Trasformata di Fourier (Segnali Aperiodici):**
  - $X(f) = \int_{-\infty}^{+\infty} x(t) e^{-j2\pi ft} dt$
- **Teorema di Parseval / Energia e Potenza:**
  - $E_x = \int |x(t)|^2 dt = \int |X(f)|^2 df$
  - Densità Spettrale di Energia: $E_x(f) \triangleq |X(f)|^2$
  - Potenza di un segnale periodico: $P_x = \sum |X_k|^2$

## 4. Sistemi Lineari Stazionari (SLS) e Filtri

- **SLS:** Sistema Lineare Stazionario (LTI - Linear Time-Invariant nella letteratura inglese).
- **Risposta impulsiva:** $h(t)$. Un sistema è _causale_ se $h(t) = h(t)u(t)$.
- **Risposta in frequenza:** $H(f) = \mathcal{F}\{h(t)\}$.
- **Relazione Ingresso-Uscita:** $Y(f) = X(f) \cdot H(f)$.
- **Decibel (dB):** Utilizzati per l'attenuazione/guadagno.
  - Per le potenze: $G_{dB} = 10 \log_{10}(P_{out}/P_{in})$
  - Per le ampiezze / FdT: $|H(f)|_{dB} \triangleq 10 \log_{10} \frac{|H(f)|^2}{|H(f_0)|^2}$ (o convenzionalmente $20 \log_{10}|H(f)|$).
- **Banda a -3dB:** Frequenza convenzionale in cui l'ampiezza in potenza si dimezza ($|H(f)|^2 = 1/2$).
- **Filtri Ideali:** $H_{LP}(f)$ (Passa-basso), $H_{HP}(f)$ (Passa-alto), $H_{BP}(f)$ (Passa-banda), $H_{BR}(f)$ (Elimina-banda / Band-reject).

## 5. Teoria delle Modulazioni

- $m(t)$ : Segnale modulante (l'informazione).
- $f_c$ : Frequenza portante (Carrier).
- $A_c$ : Ampiezza della portante.
- **AM (DSB):** $s(t) = A_c[1+m(t)]\cos(2\pi f_c t)$
- **DSB-SC (Portante Soppressa):** $s(t) = A_c m(t)\cos(2\pi f_c t)$
- **SSB (Single Side Band):** USSB (Upper) e LSSB (Lower). Generabile via Trasformata di Hilbert $\hat{m}(t)$.
- **FM / PM (Modulazioni Angolari):**
  - Fase istantanea: $\psi(t) = 2\pi f_c t + \theta(t)$.
  - Deviazione di fase: $\Delta\theta = D_p V_p$ (dove $V_p = \max|m(t)|$).
  - Deviazione di frequenza: $\Delta f = D_f V_p / 2\pi$.
  - **Regola di Carson (Banda):** $B_T = 2(\beta + 1)B$ (dove $\beta$ è l'indice di modulazione e $B$ la banda del segnale base).

## 6. Segnali e Processi Aleatori (Rumore)

- **Processo Aleatorio:** $X(t, \omega_i)$ semplificato quasi sempre in $X(t)$.
- **Valore Medio (Statistico):** $\eta_X(t) \triangleq E\{X(t)\}$ (E indica l'operatore "Valore Atteso" o Expected Value).
- **Autocorrelazione Statistica:** $R_X(t_1, t_2) \triangleq E\{X(t_1)X(t_2)\}$.
- **Autocovarianza:** $C_X(t_1, t_2) \triangleq E\{[X(t_1)-\eta_X(t_1)][X(t_2)-\eta_X(t_2)]\}$.
- **Stazionarietà:**
  - **S.S.S. (Stazionario in Senso Stretto):** Tutte le statistiche di ogni ordine sono invarianti per traslazioni temporali.
  - **WSS o S.S.L. (Stazionario in Senso Lato):** Valor medio costante ($\eta_X(t) = \eta_X$) e autocorrelazione dipendente solo dalla differenza di tempo $\tau = t_1 - t_2 \Rightarrow R_X(\tau)$.
- **Ergodicità:** Un processo è ergodico se la _media temporale_ (su una singola realizzazione) eguaglia la _media statistica_ (su tutto l'insieme - ensemble).
- **Densità Spettrale di Potenza (PSD):** $S_X(f) = \mathcal{F}\{R_X(\tau)\}$ (Teorema di Wiener-Khintchine).
- **Rumore Bianco e Termico:**
  - Spettro piatto: $S_N(f) = \text{costante}$.
  - Nelle slide il rumore termico è quantificato fisicamente come $S_N(f) = 2KTR$ (dove $K$ è la cost. di Boltzmann, $T$ la temp. in Kelvin, $R$ la resistenza). Spesso in teoria indicato genericamente come costante.
  - Autocorrelazione del rumore bianco: impulso di Dirac nell'origine $R_N(\tau) \propto \delta(\tau)$.
