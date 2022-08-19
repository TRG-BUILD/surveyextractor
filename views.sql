SELECT
   respondent_externkey,
   --answer_id,
   --respondent_survey,
   --respondent_respondentid,
   --respondent_organization,
   --l1.text as respondent_organization_text,
   --respondent_statinternal,
   --respondent_created,
   --respondent_modified,
   --respondent_closetime,
   --respondent_starttime,
   --respondent_difftime,
   --respondent_responsecollectsessions,
   --respondent_numberofreturnedmail,
   --respondent_importgroup,
   --respondent_distributionschedule,
   --respondent_email,
   --respondent_digitaldistributionstatus,
   --l2.text as respondent_digitaldistributionstatus_text,
   respondent_digitaldistributionerrormessage,
   questionnaire_samtykke,
   l3.text as questionnaire_samtykke_text,
   questionnaire_maalgruppe,
   l4.text as questionnaire_maalgruppe_text,
   questionnaire_email,
   questionnaire_del1_koerselsfrekvens,
   l5.text as questionnaire_del1_koerselsfrekvens_text,
   questionnaire_del1_koerselsomfang,
   l6.text as  questionnaire_del1_koerselsomfang_text,
FROM
   public.answers_1293731
   LEFT JOIN labels_1293731 l1 ON respondent_organization = l1.attr_id
   LEFT JOIN labels_1293731 l2 ON l2.attr_id = respondent_digitaldistributionstatus
   LEFT JOIN labels_1293731 l3 ON l3.attr_id = questionnaire_samtykke
   LEFT JOIN labels_1293731 l4 ON l4.attr_id = questionnaire_maalgruppe
   LEFT JOIN labels_1293731 l5 ON l5.attr_id = questionnaire_del1_koerselsfrekvens
   LEFT JOIN labels_1293731 l6 ON l6.attr_id = questionnaire_del1_koerselsomfang,
   LEFT JOIN labels_1293731 l7 ON l7.attr_id = questionnaire_del1_ok_overhast_by
LEFT JOIN labels_1293731 l8 ON l8.attr_id = questionnaire_del1_ok_overhast_land
LEFT JOIN labels_1293731 l9 ON l9.attr_id = questionnaire_del1_ok_overhast_mv
LEFT JOIN labels_1293731 l10 ON l10.attr_id = questionnaire_del1_frek_hastoverskrid_by
LEFT JOIN labels_1293731 l11 ON l11.attr_id = questionnaire_del1_frek_hastoverskrid_land
LEFT JOIN labels_1293731 l12 ON l12.attr_id = questionnaire_del1_frek_hastoverskrid_mv
LEFT JOIN labels_1293731 l13 ON l13.attr_id = questionnaire_del1_km_over_hastgr_by
LEFT JOIN labels_1293731 l14 ON l14.attr_id = questionnaire_del1_km_over_hastgr_land
LEFT JOIN labels_1293731 l15 ON l15.attr_id = questionnaire_del1_km_over_hastgr_mv
LEFT JOIN labels_1293731 l16 ON l16.attr_id = questionnaire_del1_hensigt_by
LEFT JOIN labels_1293731 l17 ON l17.attr_id = questionnaire_del1_hensigt_land
LEFT JOIN labels_1293731 l18 ON l18.attr_id = questionnaire_del1_hensigt_mv
LEFT JOIN labels_1293731 l19 ON l19.attr_id = questionnaire_del1_fartboeder
LEFT JOIN labels_1293731 l20 ON l20.attr_id = questionnaire_del1_klip
LEFT JOIN labels_1293731 l21 ON l21.attr_id = questionnaire_del1_bevidst_overskridelse
LEFT JOIN labels_1293731 l22 ON l22.attr_id = questionnaire_del1_paavirket_af_boede
LEFT JOIN labels_1293731 l23 ON l23.attr_id = questionnaire_del1_uddyb
LEFT JOIN labels_1293731 l24 ON l24.attr_id = questionnaire_del1_holdning_gene
LEFT JOIN labels_1293731 l25 ON l25.attr_id = questionnaire_del1_holdning_risiko
LEFT JOIN labels_1293731 l26 ON l26.attr_id = questionnaire_del1_holdning_afslappet
LEFT JOIN labels_1293731 l27 ON l27.attr_id = questionnaire_del1_holdning_monoton
LEFT JOIN labels_1293731 l28 ON l28.attr_id = questionnaire_del1_holdning_kontrol
LEFT JOIN labels_1293731 l29 ON l29.attr_id = questionnaire_del1_holdning_tid
LEFT JOIN labels_1293731 l30 ON l30.attr_id = questionnaire_del1_holdning_uforudset
LEFT JOIN labels_1293731 l31 ON l31.attr_id = questionnaire_del1_holdning_frihed
LEFT JOIN labels_1293731 l32 ON l32.attr_id = questionnaire_del1_holdning_flow
LEFT JOIN labels_1293731 l33 ON l33.attr_id = questionnaire_del1_kontrol_vilje
LEFT JOIN labels_1293731 l34 ON l34.attr_id = questionnaire_del1_kontrol_andre
LEFT JOIN labels_1293731 l35 ON l35.attr_id = questionnaire_del1_kontrol_omstaendighed
LEFT JOIN labels_1293731 l36 ON l36.attr_id = questionnaire_del1_kontrol_kanikke
LEFT JOIN labels_1293731 l37 ON l37.attr_id = questionnaire_del1_norm_lokal_overholde
LEFT JOIN labels_1293731 l38 ON l38.attr_id = questionnaire_del1_norm_bekendt_synes
LEFT JOIN labels_1293731 l39 ON l39.attr_id = questionnaire_del1_norm_grin
LEFT JOIN labels_1293731 l40 ON l40.attr_id = questionnaire_del1_norm_bekendt_overskrid
LEFT JOIN labels_1293731 l41 ON l41.attr_id = questionnaire_del1_norm_forbillede
LEFT JOIN labels_1293731 l42 ON l42.attr_id = questionnaire_del1_norm_familie
LEFT JOIN labels_1293731 l43 ON l43.attr_id = questionnaire_del1_norm_lokal_synes
LEFT JOIN labels_1293731 l44 ON l44.attr_id = questionnaire_del1_kommentar
LEFT JOIN labels_1293731 l45 ON l45.attr_id = background_cprnr
LEFT JOIN labels_1293731 l46 ON l46.attr_id = background_navn
LEFT JOIN labels_1293731 l47 ON l47.attr_id = background_postnr
LEFT JOIN labels_1293731 l48 ON l48.attr_id = background_g_dato
LEFT JOIN labels_1293731 l49 ON l49.attr_id = background_bØde
LEFT JOIN labels_1293731 l50 ON l50.attr_id = background_hastgr
LEFT JOIN labels_1293731 l51 ON l51.attr_id = background_vejtype
LEFT JOIN labels_1293731 l52 ON l52.attr_id = background_hast
LEFT JOIN labels_1293731 l53 ON l53.attr_id = background_klip
LEFT JOIN labels_1293731 l54 ON l54.attr_id = respondent_statcompletion
LEFT JOIN labels_1293731 l55 ON l55.attr_id = respondent_statcreation
LEFT JOIN labels_1293731 l56 ON l56.attr_id = respondent_statdistribution
LEFT JOIN labels_1293731 l57 ON l57.attr_id = respondent_statsource
LEFT JOIN labels_1293731 l58 ON l58.attr_id = respondent_statcollect
LEFT JOIN labels_1293731 l59 ON l59.attr_id = respondent_statoverall
LEFT JOIN labels_1293731 l60 ON l60.attr_id = calculated_gruppe

/*
limit 1
   l = ["questionnaire_del1_ok_overhast_by",
   "questionnaire_del1_ok_overhast_land",
   "questionnaire_del1_ok_overhast_mv",
   "questionnaire_del1_frek_hastoverskrid_by",
   "questionnaire_del1_frek_hastoverskrid_land",
   "questionnaire_del1_frek_hastoverskrid_mv",
   "questionnaire_del1_km_over_hastgr_by",
   "questionnaire_del1_km_over_hastgr_land",
   "questionnaire_del1_km_over_hastgr_mv",
   "questionnaire_del1_hensigt_by",
   "questionnaire_del1_hensigt_land",
   "questionnaire_del1_hensigt_mv",
   "questionnaire_del1_fartboeder",
   "questionnaire_del1_klip",
   "questionnaire_del1_bevidst_overskridelse",
   "questionnaire_del1_paavirket_af_boede",
   "questionnaire_del1_uddyb",
   "questionnaire_del1_holdning_gene",
   "questionnaire_del1_holdning_risiko",
   "questionnaire_del1_holdning_afslappet",
   "questionnaire_del1_holdning_monoton",
   "questionnaire_del1_holdning_kontrol",
   "questionnaire_del1_holdning_tid",
   "questionnaire_del1_holdning_uforudset",
   "questionnaire_del1_holdning_frihed",
   "questionnaire_del1_holdning_flow",
   "questionnaire_del1_kontrol_vilje",
   "questionnaire_del1_kontrol_andre",
   "questionnaire_del1_kontrol_omstaendighed",
   "questionnaire_del1_kontrol_kanikke",
   "questionnaire_del1_norm_lokal_overholde",
   "questionnaire_del1_norm_bekendt_synes",
   "questionnaire_del1_norm_grin",
   "questionnaire_del1_norm_bekendt_overskrid",
   "questionnaire_del1_norm_forbillede",
   "questionnaire_del1_norm_familie",
   "questionnaire_del1_norm_lokal_synes",
   "questionnaire_del1_kommentar",
   "background_cprnr",
   "background_navn",
   "background_postnr",
   "background_g_dato",
   "background_bØde",
   "background_hastgr",
   "background_vejtype",
   "background_hast",
   "background_klip",
   "respondent_statcompletion",
   "respondent_statcreation",
   "respondent_statdistribution",
   "respondent_statsource",
   "respondent_statcollect",
   "respondent_statoverall",
   "calculated_gruppe"]

def create_joins(join="lEFT JOIN", labels=f"labels_{survey_id}", items )
    for i, item in enumerate(items):
        print(f"LEFT JOIN labels_1293731 l{i} ON l{i}.attr_id = {item}")

def create_selects(text_append="_text", with_id=True):
    for i, item in enumerate(l):
        print(f"{item},")
        print(f"l{i}.text as {item}_text,")
*/