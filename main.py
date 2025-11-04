# Initialize PaddleOCR instance

from Exporter import Exporter
from OCR import PaddleOCRWrapper as OCR
from Parser import Parser
from tqdm import tqdm

if __name__ == "__main__":
    parser = Parser()
    ocr = OCR()
    exporter = Exporter()
    
    voc_list = {
        #"Bevenuti":[
        #    "input/1_bevenuti_1.PNG",
        #    "input/1_bevenuti_2.PNG",],
        #"PrimoIncontro":[
        #    "input/2_primo_incontro_1.PNG",
        #    "input/2_primo_incontro_2.PNG",
        #    "input/2_primo_incontro_3.PNG"],
        #"CheProfumo":[
        #    "input/3_che_profumo_1.PNG",
        #    "input/3_che_profumo_2.PNG",
        #    "input/3_che_profumo_3.PNG"],
        "UnAlbergo":[
            "input/3_un_albergo_1.PNG",
            "input/3_un_albergo_2.PNG",
            "input/3_un_albergo_3.PNG"],
        "NomiCosiCitta":[
            "input/4_nomi_cosi_citta_1.PNG",
            "input/4_nomi_cosi_citta_2.PNG",],
        "Rivediamo":[
            "input/5_rivediamo_1.PNG",],
        "DoveFaiLaSpessa":[
            "input/6_dove_fai_la_spessa_1.PNG",
            "input/6_dove_fai_la_spessa_2.PNG",
            "input/6_dove_fai_la_spessa_3.PNG",],
        "TiPiace":[
            "input/7_ti_piace_1.PNG",
            "input/7_ti_piace_2.PNG",
            "input/7_ti_piace_3.PNG",],
        "EStatoFantastico":[
            "input/8_e_stato_fantastico_1.PNG",
            "input/8_e_stato_fantastico_2.PNG",
            "input/8_e_stato_fantastico_3.PNG",
            "input/8_e_stato_fantastico_4.PNG",],
        "AriaDiVacanza":[
            "input/9_aria_di_vacanza_1.PNG",
            "input/9_aria_di_vacanza_2.PNG",
            "input/9_aria_di_vacanza_3.PNG",],
        "Rivediamo2":[
            "input/10_rivediamo_1.PNG",],
        "QuiSiMangiaBene":[
            "input/11_qui_si_mangia_bene_1.PNG",
            "input/11_qui_si_mangia_bene_2.PNG",
            "input/11_qui_si_mangia_bene_3.PNG",
            "input/11_qui_si_mangia_bene_4.PNG",],
        "ComeMiSta":[
            "input/12_come_mi_sta_1.PNG",
            "input/12_come_mi_sta_2.PNG",
            "input/12_come_mi_sta_3.PNG",],
        "TuttiInForma":[
            "input/13_tutti_in_forma_1.PNG",
            "input/13_tutti_in_forma_2.PNG",
            "input/13_tutti_in_forma_3.PNG",],
        "ComeACasa":[
            "input/14_come_a_casa_1.PNG",
            "input/14_come_a_casa_2.PNG",
            "input/14_come_a_casa_3.PNG",],
        "Rivediamo3":[
            "input/15_rivediamo_1.PNG",
        ]}
    bar0 = tqdm(total=len(voc_list),position=0) 
    for lection, img_list in voc_list.items():
        bar0.set_description(f"Processing {lection}")
        bar0.update(1)
        bar1 = tqdm(total=len(img_list),position=1) 
        for img_path in img_list:
            bar1.set_description(f"  Processing {img_path}")
            bar1.update(1)
            #parsed_ocr = ocr.read(img_path)
            parsed_ocr = img_path.replace("input/", "output/").removesuffix(".PNG") + "_res.json"
            results = parser.parse(parsed_ocr) 
            for result in results:
                exporter.add(result)
        exporter.save(f"processed/{lection}.txt")
    
