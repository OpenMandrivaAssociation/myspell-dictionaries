%define dictdir	%{_datadir}/dict/ooo
%define mozdictdir %{_datadir}/dict/mozilla

%bcond_without qtwebengine

Summary:	MySpell Spelling and Hyphenation dictionaries
Name:		myspell-dictionaries
Version:	26.2.0.1
Release:	1
License:	BSD/GPL/LGPL
Group:		System/Internationalization
Url:		https://lingucomponent.openoffice.org/download_dictionary.html
# https://gerrit.libreoffice.org/plugins/gitiles/dictionaries/+/master
# git clone https://git.libreoffice.org/dictionaries
Source0:	https://dev-builds.libreoffice.org/pre-releases/src/libreoffice-dictionaries-%{version}.tar.xz

##
## Sources for additional spell checking dictionaries
## Carried over from the pre-libreoffice-dictionaries package
##
Source1:	am_AM.zip
Source2:	az_AZ.zip
Source3:	cop_EG.zip
Source4:	csb_CSB.zip
Source5:	cy_GB.zip
Source6:	eu_ES.zip
Source7:	fa_FA.zip
Source8:	fa_IR.zip
Source9:	fj_FJ.zip
Source10:	fo_FO.zip
Source11:	fur_IT.zip
Source12:	fy_NL.zip
Source13:	ga_IE.zip
Source14:	gsc_FR.zip
Source15:	hy_AM.zip
Source16:	km_KH.zip
Source17:	la_LA.zip
Source18:	mg_MG.zip
Source19:	mi_NZ.zip
Source20:	ms_MY.zip
Source21:	nr_ZA.zip
Source22:	ns_ZA.zip
Source23:	ny_MW.zip
Source24:	qu_BO.zip
Source25:	rw_RW.zip
Source26:	ss_ZA.zip
Source27:	st_ZA.zip
Source28:	sw_KE.zip
Source29:	tet_ID.zip
Source30:	tl_PH.zip
Source31:	tn_ZA.zip
Source32:	ts_ZA.zip
Source33:	uz_UZ.zip
Source34:	ve_ZA.zip
Source35:	xh_ZA.zip
Source36:	zu_ZA.zip

Source50:	hyph_fi_FI.zip
Source51:	hyph_fr_BE.zip
Source52:	hyph_ga_IE.zip
BuildArch:	noarch
BuildRequires:	unzip

Source10000:	myspell-genpackages.sh

%if %{with qtwebengine}
BuildRequires:	cmake(Qt6WebEngineCore)
%endif


%description
myspell-* packages contain spell checking data to be used by
OpenOffice.org or any other MySpell-capable application, like
Mozilla. myspell-hyph-* packages contain hyphenation dictionaries for
a particular set of languages.

%{expand:%(/bin/sh %{S:10000} af_ZA "DICT          " "Afrikaans (Africa)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} am_AM "DICT          " "Amharic (Ethiopia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} an_ES "DICT          " "Aragonese" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ar "DICT          " "Arabic (North Africa and Middle East)" "Check readme" ar_AR 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} as_IN "DICT HYPH     " "Assamese" "Check readme" ar_AR 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} az_AZ "DICT          " "Azerbaijani (Azerbaijan)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} be_BY "DICT          " "Belarusian" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} bg_BG "DICT          " "Bulgarian (Bulgaria)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} bn_BD "DICT          " "Bengali (India)" "Check readme" bn_BN 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} bo "DICT          " "Classical Tibetan" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} br_FR "DICT          " "Breton" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} bs_BA "DICT          " "Bosnian" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ca "DICT          " "Catalan" GPL ca_ES 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} cop_EG "DICT          " "Coptic (North Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} cs_CZ "DICT HYPH THES" "Czech (Czech Republic)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} csb_CSB "DICT          " "Kashubian (Poland)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ckb "DICT          " "Central Kurdish" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} cy_GB "DICT          " "Welsh (Wales)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} da_DK "DICT HYPH     " "Danish (Denmark)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} de "DICT HYPH THES" "German" GPL "de_AT de_CH de_DE" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} el_GR "DICT HYPH     " "Greek (Greece)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} en "DICT HYPH THES" "English" BSD "en_AU en_CA en_GB en_NZ en_US en_ZA" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} eo "DICT HYPH THES" "Esperanto (anywhere)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} es "DICT HYPH THES" "Spanish" GPL "es_ES es_MX" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} et_EE "DICT HYPH     " "Estonian (Estonia)" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} eu_ES "DICT          " "Basque" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fa_FA "DICT          " "Farsi (Iran)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fa_IR "DICT          " "Persian (Iran)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fi_FI "     HYPH     " "Finnish (Finland)" "freely distributable" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fj_FJ "DICT          " "Fijian (Fiji)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fo_FO "DICT          " "Faroese (Faroe Islands)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fr_BE "     HYPH     " "French (Belgium)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fr_FR "DICT HYPH THES" "French (France)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fur_IT "DICT          " "Friulian (north-east Italy)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} fy_NL "DICT          " "Frisian (Netherlands)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ga_IE "DICT HYPH     " "Irish (Ireland)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} gd_GB "DICT          " "Scottish Gaelic (Scotland)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} gl "DICT          " "Galician" GPL gl_ES 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} gu_IN "DICT          " "Gujarati" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} gug "DICT          " "Guarani" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} gsc_FR "DICT          " "Gascon (France)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} he_IL "DICT          " "Hebrew (Israel)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} hi_IN "DICT          " "Hindi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} hr_HR "DICT          " "Croatian (Croatia)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} hu_HU "DICT HYPH THES" "Hungarian (Hungary)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} hy_AM "DICT          " "Armenian (Eastern and Western)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} id "DICT HYPH     " "Indonesian" GPL id_ID 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} is "DICT HYPH     " "Icelandic" LGPL is_IS 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} it_IT "DICT HYPH THES" "Italian (Italy)" LGPL/GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} km_KH "DICT          " "Khmer (Cambodia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} kn_IN "DICT          " "Kannada (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ko_KR "DICT          " "Korean" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} kmr_Latn "DICT          " "Kurdish" "Check readme" ku_TR 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} la_LA "DICT          " "Latin (x-register)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} lo_LA "DICT          " "Lao" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} lt_LT "DICT HYPH     " "Lithuanian (Lithuania)" BSD-like 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} lv_LV "DICT          " "Latvian (Latvia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} mg_MG "DICT          " "Malagasy (Madagascar)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} mi_NZ "DICT          " "Maori (New Zealand)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} mn_MN "DICT          " "Mongolian (Mongolia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} mr_IN "DICT          " "Marathi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ms_MY "DICT          " "Malay (Malaysia)" "GNU Free Documentation License" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ne_NP "DICT          " "Nepali (Nepal)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} nl_NL "DICT HYPH     " "Dutch (Netherlands)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} no "DICT          " "Norwegian" GPL "nn_NO nb_NO" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} nr_ZA "DICT          " "Ndebele (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ns_ZA "DICT          " "Northern Sotho (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ny_MW "DICT          " "Chichewa (Malawi)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} oc_FR "DICT          " "Occitan (France)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} or_IN "DICT          " "Oriya (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} pa_IN "              " "Punjabi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} pl_PL "DICT HYPH THES" "Polish (Poland)" "Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} pt_BR "DICT HYPH     " "Portuguese (Brasil)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} pt_PT "DICT HYPH     " "Portuguese (Portugal)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} qu_BO "DICT          " "Quechua (Bolivia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ro    "DICT HYPH     " "Romanian" GPL ro_RO 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ru_RU "DICT HYPH THES" "Russian (Russia)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} rw_RW "DICT          " "Kinyarwanda (Rwanda)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sa_IN "              " "Sanskrit" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} si_LK "DICT          " "Sinhala" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sk_SK "DICT HYPH THES" "Slovak (Slovak Republic)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sl_SI "DICT HYPH     " "Slovenian (Slovenia)" BSD-like 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sq_AL "DICT          " "Albanian" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sr "DICT          " "Serbian" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ss_ZA "DICT          " "Swazi/Swati (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} st_ZA "DICT          " "Southern Sotho (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sv_SE "DICT HYPH     " "Swedish (Sweden)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sw_KE "DICT          " "Kiswahili (Africa)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} sw_TZ "DICT          " "Kiswahili (East Africa) Extended Wordlist" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ta_IN "DICT          " "Tamil (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} te_IN "DICT          " "Telugu" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} tet_ID "DICT          " "Tetum (Indonesia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} th_TH "DICT          " "Thai (Thailand)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} tl_PH "DICT          " "Tagalog (Philippines)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} tn_ZA "DICT          " "Setswana (Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} tr_TR "DICT          " "Turkish" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ts_ZA "DICT          " "Tsonga (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} uk_UA "DICT HYPH     " "Ukrainian (Ukraine)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} uz_UZ "DICT          " "Uzbek (Uzbekistan)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} ve_ZA "DICT          " "Venda (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} vi "DICT          " "Vietnamese (Vietnam)" "Check readme" "vi_VI" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} xh_ZA "DICT          " "Xhosa (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{S:10000} zu_ZA "DICT          " "Zulu (South Africa)" LGPL 2>/dev/null )}

%prep
%autosetup -p1 -n libreoffice-%{version}/dictionaries
for i in %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18} %{S:19} %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28} %{S:29} %{S:30} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36}; do
	LNG=$(basename $i .zip)
	mkdir -p $LNG
	cd $LNG
	unzip $i
	[ -e README ] || echo "$LNG dictionary" >README
	cd ..
done
for i in %{S:50} %{S:51} %{S:52}; do
	LNG=$(basename $i .zip |sed -e 's,^hyph_,,')
	mkdir -p $LNG
	cd $LNG
	unzip $i
	cd ..
done

%build
# Nothing to do here...

%install
mkdir -p %{buildroot}%{_datadir}/dict/ooo %{buildroot}%{_datadir}/dict/mozilla
%if %{with qtwebengine}
mkdir -p %{buildroot}%{_datadir}/qt6/qtwebengine_dictionaries
%endif
for i in *; do
	[ -d "$i" ] || continue
	[ "$i" = "util" ] && continue

	HAVE_DICT=false
	HAVE_HYPH=false
	HAVE_THES=false

	cd "$i"

	for j in *.aff *.dic */*.aff */*.dic; do
		[ -e "$j" ] || continue
		b="$(basename $j)"
		cp $j %{buildroot}%{_datadir}/dict/ooo/
		ln -s ../ooo/$b %{buildroot}%{_datadir}/dict/mozilla/ || :
		echo %{_datadir}/dict/ooo/$b >>../$i.files
		echo %{_datadir}/dict/mozilla/$b >>../$i.files
		if echo $b |grep -q '^hyph'; then
			HAVE_HYPH=true
		else
%if %{with qtwebengine}
			if echo $j |grep -q '.dic$'; then
				%{_libdir}/qt6/libexec/qwebengine_convert_dict $j %{buildroot}%{_datadir}/qt6/qtwebengine_dictionaries/${b/.dic/.bdic} && echo %{_datadir}/qt6/qtwebengine_dictionaries/${b/.dic/.bdic} >>../$i.files || :
			fi
%endif
			HAVE_DICT=true
		fi
	done
	for j in *.dat */*.dat; do
		[ -e "$j" ] || continue
		b="$(basename $j)"
		cp $j %{buildroot}%{_datadir}/dict/ooo/
		echo %{_datadir}/dict/ooo/$b >>../$i.files
		HAVE_THES=true
	done
	for j in *.idx */*.idx; do
		[ -e "$j" ] || continue
		b="$(basename $j)"
		cp $j %{buildroot}%{_datadir}/dict/ooo/
		echo %{_datadir}/dict/ooo/$b >>../$i.files
	done

	if $HAVE_DICT; then
		mkdir -p ../doc/DICT/$i
		cp README ../doc/DICT/$i || :
		cp README_$i* ../doc/DICT/$i || :
		cp *.xml ../doc/DICT/$i || :
		cp *.xcu ../doc/DICT/$i || :
	fi
	if $HAVE_HYPH; then
		mkdir -p ../doc/HYPH/hyph_$i
		cp README_hy* ../doc/HYPH/hyph_$i || echo  "$i Hyphenation dictionary" >../doc/HYPH/hyph_$i/README_hy_$i
	fi
	if $HAVE_THES; then
		mkdir -p ../doc/THES/th_$i
		cp README_th* ../doc/THES/th_$i || echo "$i Thesaurus" >../doc/THES/th_$i/README_th_$i
	fi

	cd ..
done
