from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageNaslovna(PageBase):
    __url = "https://ovdjeisada.hr/"
    __location_pin_link_header = (By.XPATH, "")  # Missing XPATH
    __cookies_prihvati_button = (By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    __address_link_header = (By.XPATH,
                             "/html//div[@id='et-boc']/header[@class='et-l et-l--header']//div[@class='et_pb_section "
                             "et_pb_section_0_tb_header et_pb_with_background et_section_regular']/div/div[1]/div/div["
                             "@class='et_pb_code_inner']/div/div/a["
                             "@href='https://www.google.com/maps/place/Zemljakova+ul.+3,+10000,+Zagreb/@45.7727415,"
                             "15.9839423,17z/data=!3m1!4b1!4m5!3m4!1s0x4765d5df1832ecfb:0xb32333742eb30433!8m2!3d45"
                             ".7727415"
                             "!4d15.9839423']")
    __phone_link_header = (By.XPATH,
                           "/ html // div[ @ id = 'et-boc'] / header[ @ class ='et-l et-l--header'] /div[@ class "
                           "='et_builder_inner_content et_pb_gutters3'] /div[@ class ='et_pb_section "
                           "et_pb_section_0_tb_header et_pb_with_background et_section_regular'] /div/div[2] /div/div[@"
                           "class ='et_pb_code_inner'] /div // a[@ href='tel:+385958937551']")
    __facebook_icon_header = (By.XPATH, "/html//div[@id='et-boc']/header[@class='et-l et-l--header']//div["
                                        "@class='et_pb_section et_pb_section_0_tb_header et_pb_with_background "
                                        "et_section_regular']/div/div[3]/ul//a[@title='Follow on Facebook']")
    __instagram_icon_header = (By.XPATH, "/html//div[@id='et-boc']/header[@class='et-l et-l--header']//div["
                                         "@class='et_pb_section et_pb_section_0_tb_header et_pb_with_background "
                                         "et_section_regular']/div/div[3]/ul//a[@title='Follow on Instagram']")
    __ovdje_i_sada_icon_header = (By.XPATH, "/html//div[@id='et-boc']/header[@class='et-l et-l--header']/div["
                                            "@class='et_builder_inner_content et_pb_gutters3']//div["
                                            "@class='et_pb_menu__logo']/a[@href='https://ovdjeisada.hr/']/img["
                                            "@alt='Ovjde i"
                                            "sada logo tvrtke']")
    __naslovna_button_header = (By.XPATH, "// ul[ @ id = 'menu-navigation'] // a[ @ href = 'https://ovdjeisada.hr/']")
    __usluge_button_header = (By.XPATH, "//ul[@id='menu-navigation']//a[@href='https://ovdjeisada.hr/usluge/']")
    __rad_s_djecom_link_header = (By.XPATH, "// ul[ @ id = 'menu-navigation'] / li[2] / ul[ @ class ='sub-menu'] // a[@"
                                            "href='https://ovdjeisada.hr/usluge/rad-s-djecom/']")
    __rsd_individualni_savjetodavni_rad_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                                 "@class='sub-menu']/li[1]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/rad-s-djecom"
                                                                 "/djecji-psiholog/']")
    __rsd_play_attention_tretman_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li["
                                                          "1]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/play"
                                                          "-attention-tretman-za-djecu/']")
    __rsd_priprema_za_skolu_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li[1]/ul["
                                                     "@class='sub-menu']//a["
                                                     "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/priprema-za"
                                                     "-skolu/']")
    __rsd_vjezbe_opustanja_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li[1]/ul["
                                                    "@class='sub-menu']//a["
                                                    "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/vjezbe"
                                                    "-opustanja-za"
                                                    "-djecu/']")
    __rsd_radionice_za_ucenje_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li["
                                                       "1]/ul[@class='sub-menu']//a["
                                                       "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako-nauciti"
                                                       "-uciti/']")
    __rsd_i_uciti_treba_nauciti_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                         "@class='sub-menu']/li[1]/ul[@class='sub-menu']/li[5]/ul["
                                                         "@class='sub-menu']//a["
                                                         "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako"
                                                         "-nauciti-uciti/kako-nauciti-uciti-radionica/']")
    __rsd_pamti_brze_nauci_bolje_link_header = (By.XPATH,
                                                "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li[1]/ul["
                                                "@class='sub-menu']/li[5]/ul[@class='sub-menu']//a["
                                                "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako-nauciti-uciti"
                                                "/uciti-kako-uciti-radionica/']")
    __rad_s_mladima_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']//a["
                                             "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/']")
    __rsm_individualni_savjetodavni_rad_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                                 "@class='sub-menu']/li[2]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/rad-s-mladima"
                                                                 "/savjetovaliste-za-mlade/']")
    __rsm_play_attention_tretman_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                          "@class='sub-menu']/li[2]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/play"
                                                          "-attention-tretman/']")
    __rsm_vjezbe_opustanja_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li["
                                                    "2]/ul[@class='sub-menu']//a["
                                                    "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/vjezbe"
                                                    "-opustanja-i-disanja/']")
    __rsm_radionice_za_ucenje_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li["
                                                       "2]/ul[@class='sub-menu']//a["
                                                       "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/radionice"
                                                       "-kako-uciti/']")
    __rsm_i_uciti_treba_nauciti_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']/li["
                                                         "2]/ul[@class='sub-menu']/li[4]/ul[@class='sub-menu']//a["
                                                         "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/radionice"
                                                         "-kako-uciti/tecaj-kako-nauciti-uciti/']")
    __rsm_pamti_brze_nauci_bolje_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                          "@class='sub-menu']/li[2]/ul[@class='sub-menu']/li[4]/ul["
                                                          "@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-mladima"
                                                          "/radionice-kako-uciti/radionice-za-ucenje/']")
    __rad_s_odraslima_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']//a["
                                               "@href='https://ovdjeisada.hr/usluge/psiholosko-savjetovaliste/']")
    __rso_individualni_savjetodavni_rad_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                                 "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                                 "-savjetovaliste/psiholosko-savjetovanje/']")
    __rso_savjetovanje_roditelja_parova_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                                 "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                                 "-savjetovaliste/savjetovanje-za-roditelje/']")
    __rso_play_attention_tretman_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                          "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                          "-savjetovaliste/play-attention-za-odrasle/']")
    __rso_predavanja_i_grupne_podrske_link_header = (By.XPATH, "//ul[@id='menu-navigation']/li[2]/ul["
                                                               "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                               "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                               "-savjetovaliste/edukacija-za-roditelje/']")
    __blog_button_header = (By.XPATH, "//ul[@id='menu-navigation']//a[@href='https://ovdjeisada.hr/blog/']")
    __o_nama_button_header = (By.XPATH, "//ul[@id='menu-navigation']//a["
                                        "@href='https://ovdjeisada.hr/centar-za-mentalno-zdravlje/']")
    __kontakt_button_header = (By.XPATH, "//ul[@id='menu-navigation']//a[@href='https://ovdjeisada.hr/kontakt/']")
    __vidi_usluge_button_1 = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='et_builder_inner_content "
                                        "et_pb_gutters3']/div[1]/div[3]/div[2]/div[1]/a["
                                        "@href='https://ovdjeisada.hr/usluge/']")
    __o_nama_button = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='et_builder_inner_content "
                                 "et_pb_gutters3']/div[1]/div[3]/div[2]/div[2]/a["
                                 "@href='https://ovdjeisada.hr/centar-za-mentalno-zdravlje/']")
    __vidi_usluge_button_2 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                        "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/a["
                                        "@href='https://ovdjeisada.hr/usluge/']")
    __vidi_usluge_button_3 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                        "@class='et_builder_inner_content et_pb_gutters3']/div[3]/div/div[1]/div["
                                        "3]/a[@href='https://ovdjeisada.hr/usluge/']")
    __vidi_usluge_button_4 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                        "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/a["
                                        "@href='https://ovdjeisada.hr/usluge/']")
    __ovdje_link = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l "
                              "et-l--post']/div/div[3]/div/div[1]/div[2]//a[@title='Saznajte više o Ovdje i sada!']")
    __play_attention_link = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                       "@class='et-l et-l--post']/div[@class='et_builder_inner_content "
                                       "et_pb_gutters3']/div[3]/div/div[2]/div[2]/div[2]/div[1]//a[@title='Saznajte "
                                       "više o Play Attention-u']")
    __h1_header_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                  "@class='et_builder_inner_content et_pb_gutters3']/div[1]/div[1]/div[2]/div//span["
                                  ".='Ovdje i sada']")
    __h2_header_1_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                    "@class='et-l et-l--post']//h2[.='Naše usluge']")
    __h2_header_2_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                    "@class='et_pb_row et_pb_row_4']/div/div//h2[.='Naš prostor']")
    __h3_header_1_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                    "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[1]/div[2]/div[1]//h3["
                                    ".='Ovdje i sada radionice']")
    __h3_header_2_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                    "@class='et_builder_inner_content et_pb_gutters3']/div[3]/div/div[1]/div[2]//h3["
                                    ".='Savjetovanje']")
    __h3_header_3_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                    "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[2]/div[2]/div[1]//h3[.='Play"
                                    " Attention tretman']")
    __text_below_h1_header_body = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                             "@class='entry-content']//div[@class='et_builder_inner_content "
                                             "et_pb_gutters3']/div[1]/div[2]/div[2]/div//span")
    __paragraph_1_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                    "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[1]/div[2]/div[1]//p")
    __paragraph_2_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                    "@class='et_builder_inner_content et_pb_gutters3']/div[3]/div/div[1]/div[2]//p")
    __paragraph_3_body = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div["
                                    "@class='et-l et-l--post']/div/div[3]/div/div[2]/div[2]/div[2]/div[1]//p")
    __cover_image = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='et_builder_inner_content "
                               "et_pb_gutters3']/div[1]")
    __image_1 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                           "@class='et_builder_inner_content et_pb_gutters3']/div[3]/div/div[1]/div[1]//img")
    __image_2 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l "
                           "et-l--post']//div[@class='et_pb_column et_pb_column_1_4 et_pb_column_inner "
                           "et_pb_column_inner_0']/div//img[@alt='ovdje i sada - igraonice za djecu :)']")
    __image_3 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l "
                           "et-l--post']//div[@class='et_pb_column et_pb_column_1_4 et_pb_column_inner "
                           "et_pb_column_inner_2']/div//img[@alt='ovdje i sada - fotografija play attention-a']")
    __image_4 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                           "@class='et_pb_section et_pb_section_3 et_section_regular']/div[2]/div[1]/div//img["
                           "@alt='fotografija prostora od ovdje i sada ']")
    __image_5 = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                           "@class='et_pb_section et_pb_section_3 et_section_regular']/div[2]/div[2]/div//img["
                           "@alt='ovdje i sada- fogorafija našeg prostora']")
    __naslovna_button_footer = (By.XPATH, "//ul[@id='menu-navigation-1']//a[@href='https://ovdjeisada.hr/']")
    __usluge_button_footer = (By.XPATH, "//ul[@id='menu-navigation-1']//a[@href='https://ovdjeisada.hr/usluge/']")
    __rad_s_djecom_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']//a["
                                            "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/']")
    __rsd_individualni_savjetodavni_rad_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                                 "@class='sub-menu']/li[1]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/rad-s-djecom"
                                                                 "/djecji-psiholog/']")
    __rsd_play_attention_tretman_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                          "@class='sub-menu']/li[1]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/play"
                                                          "-attention-tretman-za-djecu/']")
    __rsd_priprema_za_skolu_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']/li["
                                                     "1]/ul[@class='sub-menu']//a["
                                                     "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/priprema-za"
                                                     "-skolu/']")
    __rsd_vjezbe_opustanja_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']/li["
                                                    "1]/ul[@class='sub-menu']//a["
                                                    "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/vjezbe"
                                                    "-opustanja-za-djecu/']")
    __rsd_radionice_za_ucenje_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']/li["
                                                       "1]/ul[@class='sub-menu']//a["
                                                       "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako-nauciti"
                                                       "-uciti/']")
    __rsd_i_uciti_treba_nauciti_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                         "@class='sub-menu']/li[1]/ul[@class='sub-menu']/li[5]/ul["
                                                         "@class='sub-menu']//a["
                                                         "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako"
                                                         "-nauciti-uciti/kako-nauciti-uciti-radionica/']")
    __rsd_pamti_brze_nauci_bolje_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                          "@class='sub-menu']/li[1]/ul[@class='sub-menu']/li[5]/ul["
                                                          "@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/kako"
                                                          "-nauciti-uciti/uciti-kako-uciti-radionica/']")
    __rad_s_mladima_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']//a["
                                             "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/']")
    __rsm_individualni_savjetodavni_rad_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                                 "@class='sub-menu']/li[2]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/rad-s-mladima"
                                                                 "/savjetovaliste-za-mlade/']")
    __rsm_play_attention_tretman_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                          "@class='sub-menu']/li[2]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/play"
                                                          "-attention-tretman/']")
    __rsm_vjezbe_opustanja_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']/li["
                                                    "2]/ul[@class='sub-menu']//a["
                                                    "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/vjezbe"
                                                    "-opustanja-i-disanja/']")
    __rsm_radionice_za_ucenje_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']/li["
                                                       "2]/ul[@class='sub-menu']//a["
                                                       "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/radionice"
                                                       "-kako-uciti/']")
    __rsm_i_uciti_treba_nauciti_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                         "@class='sub-menu']/li[2]/ul[@class='sub-menu']/li[4]/ul["
                                                         "@class='sub-menu']//a["
                                                         "@href='https://ovdjeisada.hr/usluge/rad-s-mladima/radionice"
                                                         "-kako-uciti/tecaj-kako-nauciti-uciti/']")
    __rsm_pamti_brze_nauci_bolje_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                          "@class='sub-menu']/li[2]/ul[@class='sub-menu']/li[4]/ul["
                                                          "@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/rad-s-mladima"
                                                          "/radionice-kako-uciti/radionice-za-ucenje/']")
    __rad_s_odraslima_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul[@class='sub-menu']//a["
                                               "@href='https://ovdjeisada.hr/usluge/psiholosko-savjetovaliste/']")
    __rso_individualni_savjetodavni_rad_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                                 "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                                 "-savjetovaliste/psiholosko-savjetovanje/']")
    __rso_savjetovanje_roditelja_parova_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                                 "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                                 "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                                 "-savjetovaliste/savjetovanje-za-roditelje/']")
    __rso_play_attention_tretman_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                          "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                          "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                          "-savjetovaliste/play-attention-za-odrasle/']")
    __rso_predavanja_i_grupne_podrske_link_footer = (By.XPATH, "//ul[@id='menu-navigation-1']/li[2]/ul["
                                                               "@class='sub-menu']/li[3]/ul[@class='sub-menu']//a["
                                                               "@href='https://ovdjeisada.hr/usluge/psiholosko"
                                                               "-savjetovaliste/edukacija-za-roditelje/']")
    __blog_button_footer = (By.XPATH, "//ul[@id='menu-navigation-1']//a[@href='https://ovdjeisada.hr/blog/']")
    __o_nama_button_footer = (By.XPATH, "//ul[@id='menu-navigation-1']//a["
                                        "@href='https://ovdjeisada.hr/centar-za-mentalno-zdravlje/']")
    __kontakt_button_footer = (By.XPATH, "//ul[@id='menu-navigation-1']//a[@href='https://ovdjeisada.hr/kontakt/']")
    __address_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']//div["
                                       "@class='et_pb_section et_pb_section_1_tb_footer et_pb_with_background "
                                       "et_section_regular']/div[1]/div[1]/div[1]/div["
                                       "@class='et_pb_code_inner']/div/div/a["
                                       "@href='https://www.google.com/maps/place/Zemljakova+ul.+3,+10000,"
                                       "+Zagreb/@45.7727415,15.9839423,"
                                       "17z/data=!3m1!4b1!4m5!3m4!1s0x4765d5df1832ecfb:0xb32333742eb30433!8m2!3d45"
                                       ".7727415!4d15.9839423']/span[.=' Zemljakova ulica 3, ']")
    __mail_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                    "@class='et_builder_inner_content et_pb_gutters3']/div[@class='et_pb_section "
                                    "et_pb_section_1_tb_footer et_pb_with_background et_section_regular']/div[1]/div["
                                    "1]/div[2]/div[@class='et_pb_code_inner']/div/a[@href='mailto:info@ovdjeisada.hr']")
    __phone_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                     "@class='et_builder_inner_content et_pb_gutters3']/div[@class='et_pb_section "
                                     "et_pb_section_1_tb_footer et_pb_with_background et_section_regular']/div["
                                     "1]/div[1]/div[3]/div[@class='et_pb_code_inner']/div//a["
                                     "@href='tel:+385958937551']")
    __facebook_icon_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']//div["
                                        "@class='et_pb_section et_pb_section_1_tb_footer et_pb_with_background "
                                        "et_section_regular']/div[2]/div[2]/ul//a[@title='Follow on Facebook']")
    __instagram_icon_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']//div["
                                         "@class='et_pb_section et_pb_section_1_tb_footer et_pb_with_background "
                                         "et_section_regular']/div[2]/div[2]/ul//a[@title='Follow on Instagram']")
    __ecom_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                    "@class='et_builder_inner_content et_pb_gutters3']/div[@class='et_pb_section "
                                    "et_pb_section_1_tb_footer et_pb_with_background et_section_regular']//a["
                                    "@href='https://e-com.hr/']")
    __torus_inc_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                         "@class='et_builder_inner_content et_pb_gutters3']/div[@class='et_pb_section "
                                         "et_pb_section_1_tb_footer et_pb_with_background et_section_regular']//a["
                                         "@href='https://torus-inc.tech/']")
    __uvecaj_kartu_link_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                            "@class='et_builder_inner_content et_pb_gutters3']/div["
                                            "@class='et_pb_section et_pb_section_1_tb_footer et_pb_with_background "
                                            "et_section_regular']//a["
                                            "@href='https://www.openstreetmap.org/?mlat=45.77270&mlon=15.98400#map=19"
                                            "/45.77270/15.98400']")
    __h4_header_footer = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                                    "@class='et_builder_inner_content et_pb_gutters3']//h4[.='Posjetite nas na našoj "
                                    "lokaciji u Novom Zagrebu']")
    __footer_text = (By.XPATH, "/html//div[@id='et-main-area']/footer[@class='et-l et-l--footer']/div["
                               "@class='et_builder_inner_content et_pb_gutters3']/div[@class='et_pb_section "
                               "et_pb_section_1_tb_footer et_pb_with_background et_section_regular']/div[2]/div["
                               "1]/div/div[@class='et_pb_text_inner']/p[1]")
    __small_map_widget_iframe = (By.XPATH, "//iframe[@height='165']")
    __small_map_widget_zoom_out_button = (By.XPATH, "/html//div[@id='map']/div["
                                                    "@class='leaflet-control-container']/div[1]/div/a[2]")
    __small_map_widget_zoom_in_button = (By.XPATH, "/html//div[@id='map']/div["
                                                   "@class='leaflet-control-container']/div[1]/div/a[1]")
    __small_map_widget_container = (By.XPATH, "//div[@id='map']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def close_cookies(self):
        super()._click(self.__cookies_prihvati_button)

    def click_location_pin_link_header(self):
        super()._click(self.__location_pin_link_header)

    def click_address_link_header(self):
        super()._cmd_click(self.__address_link_header)

    def click_phone_link_header(self):
        super()._cmd_click(self.__phone_link_header)

    def click_facebook_icon_header(self):
        super()._cmd_click(self.__facebook_icon_header)

    def click_instagram_icon_header(self):
        super()._cmd_click(self.__instagram_icon_header)

    def click_ovdje_i_sada_icon_header(self):
        super()._click(self.__ovdje_i_sada_icon_header)

    def click_naslovna_button_header(self):
        super()._click(self.__naslovna_button_header)

    def click_usluge_button_header(self):
        super()._click(self.__usluge_button_header)

    def hover_usluge_button_header(self):
        super()._hover(self.__usluge_button_header)

    def click_rad_s_djecom_link_header(self):
        super()._click(self.__rad_s_djecom_link_header)

    def hover_rad_s_djecom_link_header(self):
        super()._hover(self.__rad_s_djecom_link_header)

    def click_rsd_individualni_savjetodavni_rad_link_header(self):
        super()._click(self.__rsd_individualni_savjetodavni_rad_link_header)

    def click_rsd_play_attention_tretman_link_header(self):
        super()._click(self.__rsd_play_attention_tretman_link_header)

    def click_rsd_priprema_za_skolu_link_header(self):
        super()._click(self.__rsd_priprema_za_skolu_link_header)

    def click_rsd_vjezbe_opustanja_link_header(self):
        super()._click(self.__rsd_vjezbe_opustanja_link_header)

    def click_rsd_radionice_za_ucenje_link_header(self):
        super()._click(self.__rsd_radionice_za_ucenje_link_header)

    def hover_rsd_radionice_za_ucenje_link_header(self):
        super()._hover(self.__rsd_radionice_za_ucenje_link_header)

    def click_rsd_i_uciti_treba_nauciti_link_header(self):
        super()._click(self.__rsd_i_uciti_treba_nauciti_link_header)

    def click_rsd_pamti_brze_nauci_bolje_link_header(self):
        super()._click(self.__rsd_pamti_brze_nauci_bolje_link_header)

    def click_rad_s_mladima_link_header(self):
        super()._click(self.__rad_s_mladima_link_header)

    def hover_rad_s_mladima_link_header(self):
        super()._hover(self.__rad_s_mladima_link_header)

    def click_rsm_individualni_savjetodavni_rad_link_header(self):
        super()._click(self.__rsm_individualni_savjetodavni_rad_link_header)

    def click_rsm_play_attention_tretman_link_header(self):
        super()._click(self.__rsm_play_attention_tretman_link_header)

    def click_rsm_vjezbe_opustanja_link_header(self):
        super()._click(self.__rsm_vjezbe_opustanja_link_header)

    def click_rsm_radionice_za_ucenje_link_header(self):
        super()._click(self.__rsm_radionice_za_ucenje_link_header)

    def hover_rsm_radionice_za_ucenje_link_header(self):
        super()._hover(self.__rsm_radionice_za_ucenje_link_header)

    def click_rsm_i_uciti_treba_nauciti_link_header(self):
        super()._click(self.__rsm_i_uciti_treba_nauciti_link_header)

    def click_rsm_pamti_brze_nauci_bolje_link_header(self):
        super()._click(self.__rsm_pamti_brze_nauci_bolje_link_header)

    def click_rad_s_odraslima_link_header(self):
        super()._click(self.__rad_s_odraslima_link_header)

    def hover_rad_s_odraslima_link_header(self):
        super()._hover(self.__rad_s_odraslima_link_header)

    def click_rso_individualni_savjetodavni_rad_link_header(self):
        super()._click(self.__rso_individualni_savjetodavni_rad_link_header)

    def click_rso_savjetovanje_roditelja_parova_link_header(self):
        super()._click(self.__rso_savjetovanje_roditelja_parova_link_header)

    def click_rso_play_attention_tretman_link_header(self):
        super()._click(self.__rso_play_attention_tretman_link_header)

    def click_rso_predavanja_i_grupne_podrske_link_header(self):
        super()._click(self.__rso_predavanja_i_grupne_podrske_link_header)

    def click_blog_button_header(self):
        super()._click(self.__blog_button_header)

    def click_o_nama_button_header(self):
        super()._click(self.__o_nama_button_header)

    def click_kontakt_button_header(self):
        super()._click(self.__kontakt_button_header)

    def scroll_to_vidi_usluge_button_1(self):
        super()._scroll_to(self.__vidi_usluge_button_1)

    def click_vidi_usluge_button_1(self):
        super()._click(self.__vidi_usluge_button_1)

    def scroll_to_o_nama_button(self):
        super()._scroll_to(self.__o_nama_button)

    def click_o_nama_button(self):
        super()._click(self.__o_nama_button)

    def scroll_to_vidi_usluge_button_2(self):
        super()._scroll_to(self.__vidi_usluge_button_2)

    def click_vidi_usluge_button_2(self):
        super()._click(self.__vidi_usluge_button_2)

    def scroll_to_vidi_usluge_button_3(self):
        super()._scroll_to(self.__vidi_usluge_button_3)

    def click_vidi_usluge_button_3(self):
        super()._click(self.__vidi_usluge_button_3)

    def scroll_to_vidi_usluge_button_4(self):
        super()._scroll_to(self.__vidi_usluge_button_4)

    def click_vidi_usluge_button_4(self):
        super()._click(self.__vidi_usluge_button_4)

    def scroll_to_ovdje_link(self):
        super()._scroll_to(self.__ovdje_link)

    def click_ovdje_link(self):
        super()._click(self.__ovdje_link)

    def scroll_to_play_attention_link(self):
        super()._scroll_to(self.__play_attention_link)

    def click_play_attention_link(self):
        super()._click(self.__play_attention_link)

    def scroll_to_h1_header(self):
        super()._scroll_to(self.__h1_header_body)

    def is_displayed_h1_header(self):
        super()._is_displayed(self.__h1_header_body)

    def scroll_to_h2_header_1(self):
        super()._scroll_to(self.__h2_header_1_body)

    def is_displayed_h2_header_1(self):
        super()._is_displayed(self.__h2_header_1_body)

    def scroll_to_h2_header_2(self):
        super()._scroll_to(self.__h2_header_2_body)

    def is_displayed_h2_header_2(self):
        super()._is_displayed(self.__h2_header_2_body)

    def scroll_to_h3_header_1(self):
        super()._scroll_to(self.__h3_header_1_body)

    def is_displayed_h3_header_1(self):
        super()._is_displayed(self.__h3_header_1_body)

    def scroll_to_h3_header_2(self):
        super()._scroll_to(self.__h3_header_2_body)

    def is_displayed_h3_header_2(self):
        super()._is_displayed(self.__h3_header_2_body)

    def scroll_to_h3_header_3(self):
        super()._scroll_to(self.__h3_header_3_body)

    def is_displayed_h3_header_3(self):
        super()._is_displayed(self.__h3_header_3_body)

    def scroll_to_text_below_h1_header(self):
        super()._scroll_to(self.__text_below_h1_header_body)

    def is_displayed_text_below_h1_header(self):
        super()._is_displayed(self.__text_below_h1_header_body)

    def scroll_to_paragraph_1(self):
        super()._scroll_to(self.__paragraph_1_body)

    def is_displayed_paragraph_1(self):
        super()._is_displayed(self.__paragraph_1_body)

    def scroll_to_paragraph_2(self):
        super()._scroll_to(self.__paragraph_2_body)

    def is_displayed_paragraph_2(self):
        super()._is_displayed(self.__paragraph_2_body)

    def scroll_to_paragraph_3(self):
        super()._scroll_to(self.__paragraph_3_body)

    def is_displayed_paragraph_3(self):
        super()._is_displayed(self.__paragraph_3_body)

    def scroll_to_cover_image(self):
        super()._scroll_to(self.__cover_image)

    def is_displayed_cover_image(self):
        super()._is_displayed(self.__cover_image)

    def scroll_to_image_1(self):
        super()._scroll_to(self.__image_1)

    def is_displayed_image_1(self):
        super()._is_displayed(self.__image_1)

    def scroll_to_image_2(self):
        super()._scroll_to(self.__image_2)

    def is_displayed_image_2(self):
        super()._is_displayed(self.__image_2)

    def scroll_to_image_3(self):
        super()._scroll_to(self.__image_3)

    def is_displayed_image_3(self):
        super()._is_displayed(self.__image_3)

    def scroll_to_image_4(self):
        super()._scroll_to(self.__image_4)

    def is_displayed_image_4(self):
        super()._is_displayed(self.__image_4)

    def scroll_to_image_5(self):
        super()._scroll_to(self.__image_5)

    def is_displayed_image_5(self):
        super()._is_displayed(self.__image_5)

    def scroll_to_naslovna_button_footer(self):
        super()._scroll_to(self.__naslovna_button_footer)

    def click_naslovna_button_footer(self):
        super()._click(self.__naslovna_button_footer)

    def scroll_to_usluge_button_footer(self):
        super()._scroll_to(self.__usluge_button_footer)

    def click_usluge_button_footer(self):
        super()._click(self.__usluge_button_footer)

    def hover_usluge_button_footer(self):
        super()._hover(self.__usluge_button_footer)

    def click_rad_s_djecom_link_footer(self):
        super()._click(self.__rad_s_djecom_link_footer)

    def hover_rad_s_djecom_link_footer(self):
        super()._hover(self.__rad_s_djecom_link_footer)

    def click_rsd_individualni_savjetodavni_rad_link_footer(self):
        super()._click(self.__rsd_individualni_savjetodavni_rad_link_footer)

    def click_rsd_play_attention_tretman_link_footer(self):
        super()._click(self.__rsd_play_attention_tretman_link_footer)

    def click_rsd_priprema_za_skolu_link_footer(self):
        super()._click(self.__rsd_priprema_za_skolu_link_footer)

    def click_rsd_vjezbe_opustanja_link_footer(self):
        super()._click(self.__rsd_vjezbe_opustanja_link_footer)

    def click_rsd_radionice_za_ucenje_link_footer(self):
        super()._click(self.__rsd_radionice_za_ucenje_link_footer)

    def hover_rsd_radionice_za_ucenje_link_footer(self):
        super()._hover(self.__rsd_radionice_za_ucenje_link_footer)

    def click_rsd_i_uciti_treba_nauciti_link_footer(self):
        super()._click(self.__rsd_i_uciti_treba_nauciti_link_footer)

    def click_rsd_pamti_brze_nauci_bolje_link_footer(self):
        super()._click(self.__rsd_pamti_brze_nauci_bolje_link_footer)

    def click_rad_s_mladima_link_footer(self):
        super()._click(self.__rad_s_mladima_link_footer)

    def hover_rad_s_mladima_link_footer(self):
        super()._hover(self.__rad_s_mladima_link_footer)

    def click_rsm_individualni_savjetodavni_rad_link_footer(self):
        super()._click(self.__rsm_individualni_savjetodavni_rad_link_footer)

    def click_rsm_play_attention_tretman_link_footer(self):
        super()._click(self.__rsm_play_attention_tretman_link_footer)

    def click_rsm_vjezbe_opustanja_link_footer(self):
        super()._click(self.__rsm_vjezbe_opustanja_link_footer)

    def click_rsm_radionice_za_ucenje_link_footer(self):
        super()._click(self.__rsm_radionice_za_ucenje_link_footer)

    def hover_rsm_radionice_za_ucenje_link_footer(self):
        super()._hover(self.__rsm_radionice_za_ucenje_link_footer)

    def click_rsm_i_uciti_treba_nauciti_link_footer(self):
        super()._click(self.__rsm_i_uciti_treba_nauciti_link_footer)

    def click_rsm_pamti_brze_nauci_bolje_link_footer(self):
        super()._click(self.__rsm_pamti_brze_nauci_bolje_link_footer)

    def click_rad_s_odraslima_link_footer(self):
        super()._click(self.__rad_s_odraslima_link_footer)

    def hover_rad_s_odraslima_link_footer(self):
        super()._hover(self.__rad_s_odraslima_link_footer)

    def click_rso_individualni_savjetodavni_rad_link_footer(self):
        super()._click(self.__rso_individualni_savjetodavni_rad_link_footer)

    def click_rso_savjetovanje_roditelja_parova_link_footer(self):
        super()._click(self.__rso_savjetovanje_roditelja_parova_link_footer)

    def click_rso_play_attention_tretman_link_footer(self):
        super()._click(self.__rso_play_attention_tretman_link_footer)

    def click_rso_predavanja_i_grupne_podrske_link_footer(self):
        super()._click(self.__rso_predavanja_i_grupne_podrske_link_footer)

    def scroll_to_blog_button_footer(self):
        super()._scroll_to(self.__blog_button_footer)

    def click_blog_button_footer(self):
        super()._click(self.__blog_button_footer)

    def scroll_to_o_nama_button_footer(self):
        super()._scroll_to(self.__o_nama_button_footer)

    def click_o_nama_button_footer(self):
        super()._click(self.__o_nama_button_footer)

    def scroll_to_kontakt_button_footer(self):
        super()._scroll_to(self.__kontakt_button_footer)

    def click_kontakt_button_footer(self):
        super()._click(self.__kontakt_button_footer)

    def scroll_to_address_link_footer(self):
        super()._scroll_to(self.__address_link_footer)

    def click_address_link_footer(self):
        super()._click(self.__address_link_footer)

    def scroll_to_mail_link_footer(self):
        super()._scroll_to(self.__mail_link_footer)

    def click_mail_link_footer(self):
        super()._cmd_click(self.__mail_link_footer)

    def scroll_to_phone_link_footer(self):
        super()._scroll_to(self.__phone_link_footer)

    def click_phone_link_footer(self):
        super()._cmd_click(self.__phone_link_footer)

    def scroll_to_facebook_icon_footer(self):
        super()._scroll_to(self.__facebook_icon_footer)

    def click_facebook_icon_footer(self):
        super()._cmd_click(self.__facebook_icon_footer)

    def scroll_to_instagram_icon_footer(self):
        super()._scroll_to(self.__instagram_icon_footer)

    def click_instagram_icon_footer(self):
        super()._cmd_click(self.__instagram_icon_footer)

    def scroll_to_ecom_link_footer(self):
        super()._scroll_to(self.__ecom_link_footer)

    def click_ecom_link_footer(self):
        super()._cmd_click(self.__ecom_link_footer)

    def scroll_to_torus_inc_link_footer(self):
        super()._scroll_to(self.__torus_inc_link_footer)

    def click_torus_inc_link_footer(self):
        super()._cmd_click(self.__torus_inc_link_footer)

    def scroll_to_uvecaj_kartu_link_footer(self):
        super()._scroll_to(self.__uvecaj_kartu_link_footer)

    def click_uvecaj_kartu_link_footer(self):
        super()._cmd_click(self.__uvecaj_kartu_link_footer)

    def scroll_to_h4_header(self):
        super()._scroll_to(self.__h4_header_footer)

    def is_displayed_h4_header(self):
        super()._is_displayed(self.__h4_header_footer)

    def scroll_to_footer_text(self):
        super()._scroll_to(self.__footer_text)

    def is_displayed_footer_text(self):
        super()._is_displayed(self.__footer_text)

    def scroll_to_small_map_widget_iframe(self):
        super()._scroll_to(self.__small_map_widget_iframe)

    def switch_to_small_map_widget_iframe(self):
        super()._switch_to(self.__small_map_widget_iframe)

    def click_small_map_widget_zoom_out_button(self):
        super()._click(self.__small_map_widget_zoom_out_button)

    def click_small_map_widget_zoom_in_button(self):
        super()._click(self.__small_map_widget_zoom_in_button)

    def click_and_drag_on_small_map_widget_container(self):
        super()._click_and_drag(self.__small_map_widget_container)

    @property
    def expected_url(self) -> str:
        return self.__url
