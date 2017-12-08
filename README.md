# RESTful-API
DIE API von hubobel.de
folgende Aufrufe sind derzeit realisisert:GET: api.hubobel.de/facts.....: Uebersicht ueber alle verfuegbaren Facts mit ihrer ID
GET: api.hubobel.de/facts/'ID'.....: JSON des abgefragten Facts
GET: api.hubobel.de/facts/zufall.....: ein zufaellig ausgewaehlter Fact wird im JSON zurueck gegeben
GET: api.hubobel.de/lotto....: Liefert die letzten Zahlen von Mittwochs-, Euro- und Samstagslotto     (aus der Datenbank)
GET: api.hubobel.de/lotto/Mittwoch.....: Liefert die letzten Mottwochszahlen (aus der Datenbank)GET: api.hubobel.de/lotto/Euro.....: Liefert die letzten Eurojackpotzahlen (aus der Datenbank)
GET: api.hubobel.de/lotto/Samstag.....: Liefert die letzten Samstagszahlen (aus der Datenbank)
GET: api.hubobel.de/lotto/aktuell.....: Liefert die letzten Lottozahlen des Euro- und Mittwoch     bzw.Samstagslotto (online jeweils neu ermittelt)

POST: api.hubobel.de/lotto/6aus49/check.....: Uebergabe der 6+1 Zahlen als Liste - liefert Anzahl     der Treffer zurueck
POST: api.hubobel.de/lotto/6aus49/check.....: Uebergabe der 5+2 Zahlen als Liste - liefert Anzahl     der Treffer zurueck

...to be continued

