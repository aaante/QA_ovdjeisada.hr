import time

import pytest

from blog.page_blog import PageBlog
from kontakt.page_kontakt import PageKontakt
from misc.page_ecom import PageEcom
from misc.page_facebook import PageFacebook
from misc.page_gmaps import PageGmaps
from misc.page_gmaps_consent import PageGmapsConsent
from misc.page_instagram import PageInstagram
from misc.page_mail import PageMail
from misc.page_o_play_attentionu import PageOPlayAttentionu
from misc.page_openstreetmap import PageOpenStreetMap
from misc.page_phone import PagePhone
from misc.page_torus_inc import PageTorusInc
from o_nama.page_o_nama import PageONama
from page_naslovna import PageNaslovna
from usluge.page_usluge import PageUsluge
from usluge.rad_s_djecom.individualni_savjetodavni_rad.page_individualni_savjetodavni_rad import \
    PageRSDIndividualniSavjetodavniRad
from usluge.rad_s_djecom.page_rad_s_djecom import PageRadSDjecom
from usluge.rad_s_djecom.play_attention_tretman.page_play_attention_tretman import PageRSDPlayAttentionTretman
from usluge.rad_s_djecom.priprema_za_skolu.page_priprema_za_skolu import PagePripremaZaSkolu
from usluge.rad_s_djecom.radionice_za_ucenje.i_uciti_treba_nauciti.page_i_uciti_treba_nauciti import \
    PageRSDIUcitiTrebaNauciti
from usluge.rad_s_djecom.radionice_za_ucenje.page_radionice_za_ucenje import PageRSDRadioniceZaUcenje
from usluge.rad_s_djecom.radionice_za_ucenje.pamti_brze_nauci_bolje.page_pamti_brze_nauci_bolje import \
    PageRSDPamtiBrzeNauciBolje
from usluge.rad_s_djecom.vjezbe_opustanja.page_vjezbe_opustanja import PageRSDVjezbeOpustanja
from usluge.rad_s_mladima.individualni_savjetodavni_rad.page_individualni_savjetodavni_rad import \
    PageRSMIndividualniSavjetodavniRad
from usluge.rad_s_mladima.page_rad_s_mladima import PageRadSMladima
from usluge.rad_s_mladima.play_attention_tretman.page_play_attention_tretman import PageRSMPlayAttentionTretman
from usluge.rad_s_mladima.radionice_za_ucenje.i_uciti_treba_nauciti.page_i_uciti_treba_nauciti import \
    PageRSMIUcitiTrebaNauciti
from usluge.rad_s_mladima.radionice_za_ucenje.page_radionice_za_ucenje import PageRSMRadioniceZaUcenje
from usluge.rad_s_mladima.radionice_za_ucenje.pamti_brze_nauci_bolje.page_pamti_brze_nauci_bolje import \
    PageRSMPamtiBrzeNauciBolje
from usluge.rad_s_mladima.vjezbe_opustanja.page_vjezbe_opustanja import PageRSMVjezbeOpustanja
from usluge.rad_s_odraslima.individualni_savjetodavni_rad.page_individualni_savjetodavni_rad import \
    PageRSOIndividualniSavjetodavniRad
from usluge.rad_s_odraslima.page_rad_s_odraslima import PageRadSOdraslima
from usluge.rad_s_odraslima.play_attention_tretman.page_play_attention_tretman import PageRSOPlayAttentionTretman
from usluge.rad_s_odraslima.predavanja_i_grupne_podrske.page_predavanja_i_grupne_podrske import \
    PageRSOPredavanjaIGrupnePodrske
from usluge.rad_s_odraslima.savjetovanje_roditelja_parova.page_savjetovanje_roditelja_parova import \
    PageRSOsavjetovanjeRoditeljaParova


class TestHeader:

    # ❓INCOMPLETE👇
    @pytest.mark.naslovna
    @pytest.mark.debug
    def test_location_pin_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_location_pin_link_header()
        assert naslovna.expected_url == naslovna.current_url, "Expected URL is not the same as current URL"
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_address_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_address_link_header()
        gmaps_consent = PageGmapsConsent(driver)
        gmaps_consent.click_prihvati_sve_button()
        gmaps = PageGmaps(driver)
        assert gmaps.expected_url == gmaps.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", gmaps.expected_url)
        print("Current URL:", gmaps.current_url)
        print("Correct URL is opened")

    # ❓INCOMPLETE👇
    @pytest.mark.naslovna
    @pytest.mark.debug
    def test_phone_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_phone_link_header()
        phone = PagePhone(driver)
        assert phone.expected_url == phone.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", phone.expected_url)
        print("Current URL:", phone.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_facebook_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_facebook_icon_header()
        facebook = PageFacebook(driver)
        assert facebook.expected_url == facebook.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", facebook.expected_url)
        print("Current URL:", facebook.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_instagram_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_instagram_icon_header()
        instagram = PageInstagram(driver)
        assert instagram.expected_url == instagram.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", instagram.expected_url)
        print("Current URL:", instagram.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_ovdje_i_sada_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_ovdje_i_sada_icon_header()
        assert naslovna.expected_url == naslovna.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", naslovna.expected_url)
        print("Current URL:", naslovna.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_naslovna_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_naslovna_button_header()
        assert naslovna.expected_url == naslovna.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", naslovna.expected_url)
        print("Current URL:", naslovna.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_usluge_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_usluge_button_header()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.click_rad_s_djecom_link_header()
        rad_s_djecom = PageRadSDjecom(driver)
        assert rad_s_djecom.expected_url == rad_s_djecom.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", rad_s_djecom.expected_url)
        print("Current URL:", rad_s_djecom.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.click_rsd_individualni_savjetodavni_rad_link_header()
        individualni_savjetodavni_rad = PageRSDIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.click_rsd_play_attention_tretman_link_header()
        play_attention_tretman = PageRSDPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_priprema_za_skolu_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.click_rsd_priprema_za_skolu_link_header()
        priprema_za_skolu = PagePripremaZaSkolu(driver)
        assert priprema_za_skolu.expected_url == priprema_za_skolu.current_url, "Expected URL is not the same as " \
                                                                                "current URL"
        print("Expected URL:", priprema_za_skolu.expected_url)
        print("Current URL:", priprema_za_skolu.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_vjezbe_opustanja_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.click_rsd_vjezbe_opustanja_link_header()
        vjezbe_opustanja = PageRSDVjezbeOpustanja(driver)
        assert vjezbe_opustanja.expected_url == vjezbe_opustanja.current_url, "Expected URL is not the same as " \
                                                                              "current URL"
        print("Expected URL:", vjezbe_opustanja.expected_url)
        print("Current URL:", vjezbe_opustanja.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.click_rsd_radionice_za_ucenje_link_header()
        radionice_za_ucenje = PageRSDRadioniceZaUcenje(driver)
        assert radionice_za_ucenje.expected_url == radionice_za_ucenje.current_url, "Expected URL is not the same as " \
                                                                                    "current URL"
        print("Expected URL:", radionice_za_ucenje.expected_url)
        print("Current URL:", radionice_za_ucenje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_i_uciti_treba_nauciti_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.hover_rsd_radionice_za_ucenje_link_header()
        naslovna.click_rsd_i_uciti_treba_nauciti_link_header()
        i_uciti_treba_nauciti = PageRSDIUcitiTrebaNauciti(driver)
        assert i_uciti_treba_nauciti.expected_url == i_uciti_treba_nauciti.current_url, "Expected URL is not the same " \
                                                                                        "as current URL"
        print("Expected URL:", i_uciti_treba_nauciti.expected_url)
        print("Current URL:", i_uciti_treba_nauciti.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_pamti_brze_nauci_bolje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_djecom_link_header()
        naslovna.hover_rsd_radionice_za_ucenje_link_header()
        naslovna.click_rsd_pamti_brze_nauci_bolje_link_header()
        pamti_brze_nauci_bolje = PageRSDPamtiBrzeNauciBolje(driver)
        assert pamti_brze_nauci_bolje.expected_url == pamti_brze_nauci_bolje.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", pamti_brze_nauci_bolje.expected_url)
        print("Current URL:", pamti_brze_nauci_bolje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.click_rad_s_mladima_link_header()
        rad_s_mladima = PageRadSMladima(driver)
        assert rad_s_mladima.expected_url == rad_s_mladima.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", rad_s_mladima.expected_url)
        print("Current URL:", rad_s_mladima.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.click_rsm_individualni_savjetodavni_rad_link_header()
        individualni_savjetodavni_rad = PageRSMIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.click_rsm_play_attention_tretman_link_header()
        play_attention_tretman = PageRSMPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_vjezbe_opustanja_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.click_rsm_vjezbe_opustanja_link_header()
        vjezbe_opustanja = PageRSMVjezbeOpustanja(driver)
        assert vjezbe_opustanja.expected_url == vjezbe_opustanja.current_url, "Expected URL is not the same as " \
                                                                              "current URL"
        print("Expected URL:", vjezbe_opustanja.expected_url)
        print("Current URL:", vjezbe_opustanja.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.click_rsm_radionice_za_ucenje_link_header()
        radionice_za_ucenje = PageRSMRadioniceZaUcenje(driver)
        assert radionice_za_ucenje.expected_url == radionice_za_ucenje.current_url, "Expected URL is not the same as " \
                                                                                    "current URL"
        print("Expected URL:", radionice_za_ucenje.expected_url)
        print("Current URL:", radionice_za_ucenje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_i_uciti_treba_nauciti_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.hover_rsm_radionice_za_ucenje_link_header()
        naslovna.click_rsm_i_uciti_treba_nauciti_link_header()
        i_uciti_treba_nauciti = PageRSMIUcitiTrebaNauciti(driver)
        assert i_uciti_treba_nauciti.expected_url == i_uciti_treba_nauciti.current_url, "Expected URL is not the same " \
                                                                                        "as current URL"
        print("Expected URL:", i_uciti_treba_nauciti.expected_url)
        print("Current URL:", i_uciti_treba_nauciti.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_pamti_brze_nauci_bolje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_mladima_link_header()
        naslovna.hover_rsm_radionice_za_ucenje_link_header()
        naslovna.click_rsm_pamti_brze_nauci_bolje_link_header()
        pamti_brze_nauci_bolje = PageRSMPamtiBrzeNauciBolje(driver)
        assert pamti_brze_nauci_bolje.expected_url == pamti_brze_nauci_bolje.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", pamti_brze_nauci_bolje.expected_url)
        print("Current URL:", pamti_brze_nauci_bolje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.click_rad_s_odraslima_link_header()
        rad_s_odraslima = PageRadSOdraslima(driver)
        assert rad_s_odraslima.expected_url == rad_s_odraslima.current_url, "Expected URL is not the same as current " \
                                                                            "URL"
        print("Expected URL:", rad_s_odraslima.expected_url)
        print("Current URL:", rad_s_odraslima.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_odraslima_link_header()
        naslovna.click_rso_individualni_savjetodavni_rad_link_header()
        individualni_savjetodavni_rad = PageRSOIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_savjetovanje_roditelja_parova_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_odraslima_link_header()
        naslovna.click_rso_savjetovanje_roditelja_parova_link_header()
        savjetovanje_roditelja_parova = PageRSOsavjetovanjeRoditeljaParova(driver)
        assert savjetovanje_roditelja_parova.expected_url == savjetovanje_roditelja_parova.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", savjetovanje_roditelja_parova.expected_url)
        print("Current URL:", savjetovanje_roditelja_parova.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_odraslima_link_header()
        naslovna.click_rso_play_attention_tretman_link_header()
        play_attention_tretman = PageRSOPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_predavanja_i_grupne_podrske_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.hover_usluge_button_header()
        naslovna.hover_rad_s_odraslima_link_header()
        naslovna.click_rso_predavanja_i_grupne_podrske_link_header()
        predavanja_i_grupne_podrske = PageRSOPredavanjaIGrupnePodrske(driver)
        assert predavanja_i_grupne_podrske.expected_url == predavanja_i_grupne_podrske.current_url, "Expected URL is " \
                                                                                                    "not the " \
                                                                                                    "same as current " \
                                                                                                    "URL"
        print("Expected URL:", predavanja_i_grupne_podrske.expected_url)
        print("Current URL:", predavanja_i_grupne_podrske.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_blog_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_blog_button_header()
        blog = PageBlog(driver)
        assert blog.expected_url == blog.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", blog.expected_url)
        print("Current URL:", blog.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_o_nama_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_o_nama_button_header()
        o_nama = PageONama(driver)
        assert o_nama.expected_url == o_nama.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", o_nama.expected_url)
        print("Current URL:", o_nama.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_kontakt_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.click_kontakt_button_header()
        kontakt = PageKontakt(driver)
        assert kontakt.expected_url == kontakt.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", kontakt.expected_url)
        print("Current URL:", kontakt.current_url)
        print("Correct URL is opened")


class TestBody:

    @pytest.mark.naslovna
    def test_vidi_usluge_button_1(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_vidi_usluge_button_1()
        naslovna.click_vidi_usluge_button_1()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_o_nama_button(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_o_nama_button()
        naslovna.click_o_nama_button()
        o_nama = PageONama(driver)
        assert o_nama.expected_url == o_nama.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", o_nama.expected_url)
        print("Current URL:", o_nama.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_vidi_usluge_button_2(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_vidi_usluge_button_2()
        naslovna.click_vidi_usluge_button_2()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_vidi_usluge_button_3(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_vidi_usluge_button_3()
        naslovna.click_vidi_usluge_button_3()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_vidi_usluge_button_4(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_vidi_usluge_button_4()
        naslovna.click_vidi_usluge_button_4()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_ovdje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_ovdje_link()
        naslovna.click_ovdje_link()
        o_nama = PageONama(driver)
        assert o_nama.expected_url == o_nama.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", o_nama.expected_url)
        print("Current URL:", o_nama.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_play_attention_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_play_attention_link()
        naslovna.click_play_attention_link()
        o_play_attentionu = PageOPlayAttentionu(driver)
        assert o_play_attentionu.expected_url == o_play_attentionu.current_url, "Expected URL is not the same as " \
                                                                                "current URL"
        print("Expected URL:", o_play_attentionu.expected_url)
        print("Current URL:", o_play_attentionu.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_h1_header(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h1_header()
        naslovna.is_displayed_h1_header()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_h2_header_1(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h2_header_1()
        naslovna.is_displayed_h2_header_1()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_h2_header_2(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h2_header_2()
        naslovna.is_displayed_h2_header_2()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_h3_header_1(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h3_header_1()
        naslovna.is_displayed_h3_header_1()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_h3_header_2(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h3_header_2()
        naslovna.is_displayed_h3_header_2()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_h3_header_3(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h3_header_3()
        naslovna.is_displayed_h3_header_3()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_text_below_h1_header(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_text_below_h1_header()
        naslovna.is_displayed_text_below_h1_header()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_paragraph_1(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_paragraph_1()
        naslovna.is_displayed_paragraph_1()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_paragraph_2(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_paragraph_2()
        naslovna.is_displayed_paragraph_2()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_paragraph_3(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_paragraph_3()
        naslovna.is_displayed_paragraph_3()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_cover_image(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_cover_image()
        naslovna.is_displayed_cover_image()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_image_1(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_image_1()
        naslovna.is_displayed_image_1()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_image_2(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_image_2()
        naslovna.is_displayed_image_2()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_image_3(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_image_3()
        naslovna.is_displayed_image_3()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_image_4(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_image_4()
        naslovna.is_displayed_image_4()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_image_5(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_image_5()
        naslovna.is_displayed_image_5()
        print("Element is displayed")


class TestFooter:

    @pytest.mark.naslovna
    def test_naslovna_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_naslovna_button_footer()
        naslovna.click_naslovna_button_footer()
        assert naslovna.expected_url == naslovna.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", naslovna.expected_url)
        print("Current URL:", naslovna.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_usluge_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.click_usluge_button_footer()
        usluge = PageUsluge(driver)
        assert usluge.expected_url == usluge.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", usluge.expected_url)
        print("Current URL:", usluge.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.click_rad_s_djecom_link_footer()
        rad_s_djecom = PageRadSDjecom(driver)
        assert rad_s_djecom.expected_url == rad_s_djecom.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", rad_s_djecom.expected_url)
        print("Current URL:", rad_s_djecom.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.click_rsd_individualni_savjetodavni_rad_link_footer()
        individualni_savjetodavni_rad = PageRSDIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.click_rsd_play_attention_tretman_link_footer()
        play_attention_tretman = PageRSDPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_priprema_za_skolu_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.click_rsd_priprema_za_skolu_link_footer()
        priprema_za_skolu = PagePripremaZaSkolu(driver)
        assert priprema_za_skolu.expected_url == priprema_za_skolu.current_url, "Expected URL is not the same as " \
                                                                                "current URL"
        print("Expected URL:", priprema_za_skolu.expected_url)
        print("Current URL:", priprema_za_skolu.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_vjezbe_opustanja_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.click_rsd_vjezbe_opustanja_link_footer()
        vjezbe_opustanja = PageRSDVjezbeOpustanja(driver)
        assert vjezbe_opustanja.expected_url == vjezbe_opustanja.current_url, "Expected URL is not the same as " \
                                                                              "current URL"
        print("Expected URL:", vjezbe_opustanja.expected_url)
        print("Current URL:", vjezbe_opustanja.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.click_rsd_radionice_za_ucenje_link_footer()
        radionice_za_ucenje = PageRSDRadioniceZaUcenje(driver)
        assert radionice_za_ucenje.expected_url == radionice_za_ucenje.current_url, "Expected URL is not the same as " \
                                                                                    "current URL"
        print("Expected URL:", radionice_za_ucenje.expected_url)
        print("Current URL:", radionice_za_ucenje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_i_uciti_treba_nauciti_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.hover_rsd_radionice_za_ucenje_link_footer()
        naslovna.click_rsd_i_uciti_treba_nauciti_link_footer()
        i_uciti_treba_nauciti = PageRSDIUcitiTrebaNauciti(driver)
        assert i_uciti_treba_nauciti.expected_url == i_uciti_treba_nauciti.current_url, "Expected URL is not the same " \
                                                                                        "as current URL"
        print("Expected URL:", i_uciti_treba_nauciti.expected_url)
        print("Current URL:", i_uciti_treba_nauciti.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_djecom_radionice_za_ucenje_pamti_brze_nauci_bolje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_djecom_link_footer()
        naslovna.hover_rsd_radionice_za_ucenje_link_footer()
        naslovna.click_rsd_pamti_brze_nauci_bolje_link_footer()
        pamti_brze_nauci_bolje = PageRSDPamtiBrzeNauciBolje(driver)
        assert pamti_brze_nauci_bolje.expected_url == pamti_brze_nauci_bolje.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", pamti_brze_nauci_bolje.expected_url)
        print("Current URL:", pamti_brze_nauci_bolje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.click_rad_s_mladima_link_footer()
        rad_s_mladima = PageRadSMladima(driver)
        assert rad_s_mladima.expected_url == rad_s_mladima.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", rad_s_mladima.expected_url)
        print("Current URL:", rad_s_mladima.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.click_rsm_individualni_savjetodavni_rad_link_footer()
        individualni_savjetodavni_rad = PageRSMIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.click_rsm_play_attention_tretman_link_footer()
        play_attention_tretman = PageRSMPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_vjezbe_opustanja_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.click_rsm_vjezbe_opustanja_link_footer()
        vjezbe_opustanja = PageRSMVjezbeOpustanja(driver)
        assert vjezbe_opustanja.expected_url == vjezbe_opustanja.current_url, "Expected URL is not the same as " \
                                                                              "current URL"
        print("Expected URL:", vjezbe_opustanja.expected_url)
        print("Current URL:", vjezbe_opustanja.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.click_rsm_radionice_za_ucenje_link_footer()
        radionice_za_ucenje = PageRSMRadioniceZaUcenje(driver)
        assert radionice_za_ucenje.expected_url == radionice_za_ucenje.current_url, "Expected URL is not the same as " \
                                                                                    "current URL"
        print("Expected URL:", radionice_za_ucenje.expected_url)
        print("Current URL:", radionice_za_ucenje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_i_uciti_treba_nauciti_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.hover_rsm_radionice_za_ucenje_link_footer()
        naslovna.click_rsm_i_uciti_treba_nauciti_link_footer()
        i_uciti_treba_nauciti = PageRSMIUcitiTrebaNauciti(driver)
        assert i_uciti_treba_nauciti.expected_url == i_uciti_treba_nauciti.current_url, "Expected URL is not the same " \
                                                                                        "as current URL"
        print("Expected URL:", i_uciti_treba_nauciti.expected_url)
        print("Current URL:", i_uciti_treba_nauciti.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_mladima_radionice_za_ucenje_pamti_brze_nauci_bolje_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_mladima_link_footer()
        naslovna.hover_rsm_radionice_za_ucenje_link_footer()
        naslovna.click_rsm_pamti_brze_nauci_bolje_link_footer()
        pamti_brze_nauci_bolje = PageRSMPamtiBrzeNauciBolje(driver)
        assert pamti_brze_nauci_bolje.expected_url == pamti_brze_nauci_bolje.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", pamti_brze_nauci_bolje.expected_url)
        print("Current URL:", pamti_brze_nauci_bolje.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.click_rad_s_odraslima_link_footer()
        rad_s_odraslima = PageRadSOdraslima(driver)
        assert rad_s_odraslima.expected_url == rad_s_odraslima.current_url, "Expected URL is not the same as current " \
                                                                            "URL"
        print("Expected URL:", rad_s_odraslima.expected_url)
        print("Current URL:", rad_s_odraslima.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_individualni_savjetodavni_rad_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_odraslima_link_footer()
        naslovna.click_rso_individualni_savjetodavni_rad_link_footer()
        individualni_savjetodavni_rad = PageRSOIndividualniSavjetodavniRad(driver)
        assert individualni_savjetodavni_rad.expected_url == individualni_savjetodavni_rad.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", individualni_savjetodavni_rad.expected_url)
        print("Current URL:", individualni_savjetodavni_rad.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_savjetovanje_roditelja_parova_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_odraslima_link_footer()
        naslovna.click_rso_savjetovanje_roditelja_parova_link_footer()
        savjetovanje_roditelja_parova = PageRSOsavjetovanjeRoditeljaParova(driver)
        assert savjetovanje_roditelja_parova.expected_url == savjetovanje_roditelja_parova.current_url, "Expected URL " \
                                                                                                        "is not the " \
                                                                                                        "same as " \
                                                                                                        "current URL"
        print("Expected URL:", savjetovanje_roditelja_parova.expected_url)
        print("Current URL:", savjetovanje_roditelja_parova.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_play_attention_tretman_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_odraslima_link_footer()
        naslovna.click_rso_play_attention_tretman_link_footer()
        play_attention_tretman = PageRSOPlayAttentionTretman(driver)
        assert play_attention_tretman.expected_url == play_attention_tretman.current_url, "Expected URL is not the " \
                                                                                          "same as current URL"
        print("Expected URL:", play_attention_tretman.expected_url)
        print("Current URL:", play_attention_tretman.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_rad_s_odraslima_predavanja_i_grupne_podrske_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_usluge_button_footer()
        naslovna.hover_usluge_button_footer()
        naslovna.hover_rad_s_odraslima_link_footer()
        naslovna.click_rso_predavanja_i_grupne_podrske_link_footer()
        predavanja_i_grupne_podrske = PageRSOPredavanjaIGrupnePodrske(driver)
        assert predavanja_i_grupne_podrske.expected_url == predavanja_i_grupne_podrske.current_url, "Expected URL is " \
                                                                                                    "not the " \
                                                                                                    "same as current " \
                                                                                                    "URL"
        print("Expected URL:", predavanja_i_grupne_podrske.expected_url)
        print("Current URL:", predavanja_i_grupne_podrske.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_blog_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_blog_button_footer()
        naslovna.click_blog_button_footer()
        blog = PageBlog(driver)
        assert blog.expected_url == blog.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", blog.expected_url)
        print("Current URL:", blog.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_o_nama_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_o_nama_button_footer()
        naslovna.click_o_nama_button_footer()
        o_nama = PageONama(driver)
        assert o_nama.expected_url == o_nama.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", o_nama.expected_url)
        print("Current URL:", o_nama.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_kontakt_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_kontakt_button_footer()
        naslovna.click_kontakt_button_footer()
        kontakt = PageKontakt(driver)
        assert kontakt.expected_url == kontakt.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", kontakt.expected_url)
        print("Current URL:", kontakt.current_url)
        print("Correct URL is opened")

    # ❓INCOMPLETE👇
    @pytest.mark.naslovna
    @pytest.mark.debug
    def test_address_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_address_link_footer()
        naslovna.click_address_link_footer()
        gmaps_consent = PageGmapsConsent(driver)
        gmaps_consent.click_prihvati_sve_button()
        gmaps = PageGmaps(driver)
        assert gmaps.expected_url == gmaps.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", gmaps.expected_url)
        print("Current URL:", gmaps.current_url)
        print("Correct URL is opened")

    # ❓INCOMPLETE👇
    @pytest.mark.naslovna
    @pytest.mark.debug
    def test_mail_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_mail_link_footer()
        naslovna.click_mail_link_footer()
        mail = PageMail(driver)
        assert mail.expected_url == mail.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", mail.expected_url)
        print("Current URL:", mail.current_url)
        print("Correct URL is opened")

    # ❓INCOMPLETE👇
    @pytest.mark.naslovna
    @pytest.mark.debug
    def test_phone_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_phone_link_footer()
        naslovna.click_phone_link_footer()
        phone = PagePhone(driver)
        assert phone.expected_url == phone.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", phone.expected_url)
        print("Current URL:", phone.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_facebook_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_facebook_icon_footer()
        naslovna.click_facebook_icon_footer()
        facebook = PageFacebook(driver)
        assert facebook.expected_url == facebook.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", facebook.expected_url)
        print("Current URL:", facebook.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_instagram_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_instagram_icon_footer()
        naslovna.click_instagram_icon_footer()
        instagram = PageInstagram(driver)
        assert instagram.expected_url == instagram.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", instagram.expected_url)
        print("Current URL:", instagram.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_ecom_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_ecom_link_footer()
        naslovna.click_ecom_link_footer()
        ecom = PageEcom(driver)
        assert ecom.expected_url == ecom.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", ecom.expected_url)
        print("Current URL:", ecom.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_torus_inc_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_torus_inc_link_footer()
        naslovna.click_torus_inc_link_footer()
        torus_inc = PageTorusInc(driver)
        assert torus_inc.expected_url == torus_inc.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", torus_inc.expected_url)
        print("Current URL:", torus_inc.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_uvecaj_kartu_link(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_uvecaj_kartu_link_footer()
        naslovna.click_uvecaj_kartu_link_footer()
        openstreetmap = PageOpenStreetMap(driver)
        assert openstreetmap.expected_url == openstreetmap.current_url, "Expected URL is not the same as current URL"
        print("Expected URL:", openstreetmap.expected_url)
        print("Current URL:", openstreetmap.current_url)
        print("Correct URL is opened")

    @pytest.mark.naslovna
    def test_h4_header(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_h4_header()
        naslovna.is_displayed_h4_header()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_footer_text(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_footer_text()
        naslovna.is_displayed_footer_text()
        print("Element is displayed")

    @pytest.mark.naslovna
    def test_small_map_widget(self, driver):
        naslovna = PageNaslovna(driver)
        naslovna.open()
        naslovna.close_cookies()
        naslovna.scroll_to_small_map_widget_iframe()
        naslovna.switch_to_small_map_widget_iframe()
        naslovna.click_small_map_widget_zoom_out_button()
        naslovna.click_small_map_widget_zoom_in_button()
        naslovna.click_and_drag_on_small_map_widget_container()
        print("Small map widget is functional")
