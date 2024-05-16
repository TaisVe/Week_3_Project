#FUNCTION TO EXTRACT VARIETY FROM NAME IN VIVINO DF

def name_wines(string):
    for item in string:
        if "Pinot Noir" in string:
            return "Pinot Noir"
        elif "Sauvignon Blanc" in string:
            return "Sauvignon Blanc"
        elif "Pinot Gris" in string:
            return "Pinot Gris"
        elif "Pinot Grigio" in string:
            return "Pinot Grigio"
        elif "Pinot Blanc" in string:
            return "Pinot Blanc"
        elif "Moscato" in string:
            return "Moscato"
        elif "Chardonnay" in string:
            return "Chardonnay"
        elif "Cabernet Franc" in string:
            return "Cabernet Franc"
        elif "Cabernet Sauvignon" in string:
            return "Cabernet Sauvignon"
        elif "Centesimino" in string:
            return "Centesimino"
        elif "Cabernet" in string:
            return "Cabernet"
        elif "Colorino" in string:
            return "Colorino"
        elif "Jampal" in string:
            return "Jampal"
        elif "Chancellor" in string:
            return "Chancellor"
        elif "Favorita" in string:
            return "Favorita"
        elif "Sirica" in string:
            return "Sirica"
        elif "Red Blend" in string:
            return "Red Blend"
        elif "Pomerol" in string:
            return "Pomerol"
        elif "Riesling" in string:
            return "Riesling"
        elif "Rosé" in string:
            return "Rosé"
        elif "Primitivo" in string:
            return "Primitivo"
        elif "Zinfandel" in string:
            return "Zinfandel"
        elif "Rosato" in string:
            return "Rosato"
        elif "Graciano" in string:
            return "Graciano"
        elif "Crianza" in string:
            return "Crianza"
        elif "Azul" in string:
            return "Azul"
        elif "Alleanza" in string:
            return "Alleanza"
        elif "Barbera" in string:
            return "Barbera"
        elif "Meritage" in string:
            return "Meritage"
        elif "Tinto" in string:
            return "Tinto"
        elif "Blaufränkisch" in string:
            return "Blaufränkisch"
        elif "Viognier" in string:
            return "Viognier"
        elif "Syrah" in string:
            return "Syrah"
        elif "Tempus" in string:
            return "Tempus"
        elif "Pannobile" in string:
            return "Pannobile"
        elif "Ventoux" in string:
            return "Ventoux"
        elif "Nero" in string:
            return "Nero"
        elif "Malbec" in string:
            return "Malbec"
        elif "Verdejo" in string:
            return "Verdejo"
        elif "Sestal" in string:
            return "Sestal"
        elif "Verdejo" in string:
            return "Verdejo"
        elif "Prima" in string:
            return "Prima"
        elif "Prosecco" in string:
            return "Prosecco"
        elif "Champagne" in string:
            return "Champagne"
        elif "Rosso" in string:
            return "Rosso"
        elif "Maestro" in string:
            return "Maestro"
        elif "Chianti" in string:
            return "Chianti"
        elif "Red Blend" in string:
            return "Red Blend"
        elif "Cabernet" in string:
            return "Cabernet"
        elif "Gigondas" in string:
            return "Gigondas"
        elif "Fronsac" in string:
            return "Fronsac"
        elif "Bordeaux" in string:
            return "Bordeaux"
        elif "Haut" in string:
            return "Haut"
        elif "Muscat" in string:
            return "Muscat"
        elif "Sangiovese" in string:
            return "Sangiovese"
        elif "Tempranilo" in string:
            return "Tempranilo"
        else: 
            return string