# Week 5 - Security Opdracht

## Installatie

1. Zorg dat je **Python 3.13** hebt geïnstalleerd.
2. Maak een python venv aan in de projectdirectory:
```
python -m venv venv
```
3. Activeer de venv:
   - Windows:
```
 ./venv/Scripts/activate
```
   - macOS/Linux:
```
 source venv/bin/activate
```
4. Installeer de benodigde dependencies
```
   pip install -r requirements.txt
```

## Database en HSM Initialisatie

1. Genereer de database door het script uit te voeren:
```python db_gen.py```
2. Start de HSM (Hardware Security Module) simulatie:
```python hsm.py```

    De HSM moet aanblijven staan om de keys opgeslagen te houden
## Applicatie starten

1. Start de hoofdapplicatie:
   ```python main.py```
2. In de applicatie kun je nu:
   - De **zender** en **ontvanger** selecteren in het bovenste formulier.
   
     Let op: de zender mag niet hetzelfde zijn als de ontvanger.
   - Schrijf een bericht in het tekstvak.
   
![Zender & ontvanger selecteren](readme%20images/sender_reciever.png)

3. Om het bericht te **encrypten**, klik je op de encryptie-knop:

![Encryptie knop](readme%20images/send.png)

4. Wacht een paar seconden; het resultaat van de encryptie verschijnt:

![Encryptie resultaat](readme%20images/encryption_result.png)

5. Om een bericht te **decrypten**, selecteer je de gebruiker naar wie het bericht is gestuurd.
   Wacht enkele seconden en het resultaat verschijnt naast het bericht:

![Decryptie bericht](readme%20images/decrypt_message.png)
![Voorbeeld](readme%20images/img.png)