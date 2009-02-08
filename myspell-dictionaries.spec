%define dictdir	%{_datadir}/dict/ooo
%define mozdictdir %{_datadir}/dict/mozilla

%define _binary_payload w9.lzdio

Summary:	MySpell Spelling and Hyphenation dictionaries
Name:		myspell-dictionaries
Version:	1.0.2
Release:	%mkrel 24
License:	BSD/GPL/LGPL
Group:		System/Internationalization
URL:		http://lingucomponent.openoffice.org/download_dictionary.html
Source0:	myspell-genpackages.sh
BuildArch:	noarch
BuildRequires:	unzip
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

##
## Sources for spell checking dictionaries
##

Source100: bg_BG.zip
Source101: ca_ES.zip
Source102: hr_HR.zip
Source103: cs_CZ.zip
Source104: da_DK.zip

# From https://www.uitwisselplatform.nl/frs/?group_id=9
Source105: nl_NL.zip

Source106: en_CA.zip
Source107: en_GB.zip
Source108: en_US.zip
Source109: fr_FR.zip
# This is actually de_DE_comb renamed in order to not mess the current spec.
Source110: de_DE.zip
Source111: de_CH.zip
Source112: el_GR.zip
Source113: hu_HU.zip
Source114: it_IT.zip

# (tpg) MySpell dictionary comes from http://www.sjp.pl/slownik/ort/
# unzip http://sjp.pl/slownik/ort/sjp-myspell-pl-20080825.zip
Source115: pl_PL.zip

Source116: pt_PT.zip
Source117: pt_BR.zip
Source118: es_ES.zip
Source119: sk_SK.zip
Source120: sv_SE.zip
Source121: nb_NO.zip
Source122: nn_NO.zip
Source123: ga_IE.zip
Source124: gl_ES.zip
Source125: ru_RU.zip
Source126: sl_SI.zip
Source127: uk_UA.zip
Source128: de_AT.zip
Source129: en_AU.zip
Source130: es_MX.zip
Source131: fo_FO.zip
Source132: lt_LT.zip

Source133: ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/et_EE.zip

# http://sourceforge.net/project/showfiles.php?group_id=91920
Source134: af_ZA.zip

Source135: cy_GB.zip
Source136: en_NZ.zip
Source137: id_ID.zip
Source138: zu_ZA.zip
Source139: ro_RO.zip
Source140: mi_NZ.zip
Source141: sw_KE.zip
Source142: ms_MY.zip

Source143: am_AM.zip
Source144: ar_AR.zip
Source145: az_AZ.zip
Source146: bn_BN.zip
Source147: cop_EG.zip
Source148: csb_CSB.zip
Source149: en_ZA.zip
Source150: eo_EO.zip
Source151: eu_ES.zip
Source152: fa_FA.zip
Source153: fa_IR.zip
Source155: fj_FJ.zip
Source156: fur_IT.zip
Source157: fy_NL.zip
Source158: gd_GB.zip
Source159: gsc_FR.zip
Source160: he_IL.zip
Source161: hi_IN.zip
Source162: hy_AM.zip
Source164: is_IS.zip
Source163: th_TH.zip
Source165: km_KH.zip
Source166: ku_TR.zip
Source167: la_LA.zip
Source168: lv_LV.zip
Source169: mg_MG.zip
Source170: mn_MN.zip
Source171: mr_IN.zip
Source172: ne_NP.zip
Source173: nr_ZA.zip
Source174: ns_ZA.zip
Source175: ny_MW.zip
Source176: oc_FR.zip
Source177: or_OR.zip
Source178: pa_PA.zip
Source179: qu_BO.zip
Source180: rw_RW.zip
Source181: ss_ZA.zip
Source182: st_ZA.zip
Source183: sw_TZ.zip
Source184: ta_TA.zip
Source185: tet_ID.zip
Source186: tl_PH.zip
Source187: tn_ZA.zip
Source188: ts_ZA.zip
Source190: uz_UZ.zip
Source191: ve_ZA.zip
Source192: vi_VI.zip
Source193: xh_ZA.zip

##
## Sources for hyphenation dictionaries
##

# See http://bgoffice.sourceforge.net/ooo/index.html
Source200: hyph_bg_BG.zip
Source201: hyph_cs_CZ.zip
Source202: hyph_da_DK.zip
Source203: hyph_de_CH.zip
Source204: hyph_de_DE.zip
Source205: hyph_el_GR.zip
Source206: hyph_en_CA.zip
Source207: hyph_en_GB.zip
Source208: hyph_en_US.zip
Source209: hyph_es_ES.zip
Source210: hyph_et_EE.zip
Source211: hyph_fi_FI.zip
Source212: hyph_fr_BE.zip
Source213: hyph_fr_FR.zip
Source214: hyph_ga_IE.zip
Source215: hyph_hu_HU.zip
Source216: hyph_id_ID.zip
Source217: hyph_is_IS.zip
Source218: hyph_it_IT.zip
Source219: hyph_lt_LT.zip
Source220: hyph_nl_NL.zip
Source221: hyph_pl_PL.zip
Source222: hyph_pt_BR.zip
Source223: hyph_pt_PT.zip
Source224: hyph_ro_RO.zip
Source225: hyph_ru_RU.zip
Source226: hyph_sk_SK.zip
Source227: hyph_sl_SI.zip
Source228: hyph_sv_SE.zip
Source229: hyph_uk_UA.zip

##
## Sources for hyphenation dictionaries
##

Source300: th_en_US.zip
Source301: th_fr_FR.zip
# http://it.openoffice.org/contribuire/thesaurus.html (alpha version!!!)
Source302: th_it_IT.zip
Source303: th_de_DE.zip
# http://synonimy.sourceforge.net/
Source304: th_pl_PL.zip
Source305: th_es_ES.zip
## http://bgoffice.sourceforge.net/ooo/
Source306: th_bg_BG.zip
Source307: th_sk_SK.zip

Source309: th_cs_CZ.zip
Source310: th_de_CH.zip
Source311: th_hu_HU.zip
Source312: th_ru_RU.zip

##
## Packages information
##

%description
myspell-* packages contain spell checking data to be used by
OpenOffice.org or any other MySpell-capable application, like
Mozilla. myspell-hyph-* packages contain hyphenation dictionaries for
a particular set of languages.

%{expand:%(/bin/sh %{SOURCE0} af_ZA "DICT          " "Afrikaans (Africa)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} am_AM "DICT          " "Amharic (Ethiopia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ar_AR "DICT          " "Arabic (North Africa and Middle East)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} az_AZ "DICT          " "Azerbaijani (Azerbaijan)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} bg_BG "DICT          " "Bulgarian (Bulgaria)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} bn_BN "DICT          " "Bengali (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ca_ES "DICT          " "Catalan" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} cop_EG "DICT          " "Coptic (North Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} cs_CZ "DICT HYPH THES" "Czech (Czech Republic)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} csb_CSB "DICT          " "Kashubian (Poland)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} cy_GB "DICT          " "Welsh (Wales)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} da_DK "DICT HYPH     " "Danish (Denmark)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} de_AT "DICT          " "German (Austria)"  GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} de_CH "DICT HYPH THES" "German (Switzerland)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} de_DE "DICT HYPH THES" "German (Germany)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} el_GR "DICT HYPH     " "Greek (Greece)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_AU "DICT          " "English (Australian)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_CA "DICT HYPH     " "English (Canada)" "Public Domain" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_GB "DICT HYPH     " "English (United Kingdom)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_NZ "DICT          " "English (New Zealand)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_US "DICT HYPH THES" "English (US)" BSD 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} en_ZA "DICT          " "English (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} eo_EO "DICT          " "Esperanto (anywhere)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} es_ES "DICT HYPH THES" "Spanish (Spain)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} es_MX "DICT          " "Spanish (Mexico)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} et_EE "DICT HYPH     " "Estonian (Estonia)" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} eu_ES "DICT          " "Basque" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fa_FA "DICT          " "Farsi (Iran)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fa_IR "DICT          " "Persian (Iran)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fi_FI "     HYPH     " "Finnish (Finland)" "freely distributable" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fj_FJ "DICT          " "Fijian (Fiji)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fo_FO "DICT          " "Faroese (Faroe Islands)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fr_BE "     HYPH     " "French" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fr_FR "DICT HYPH THES" "French (France)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fur_IT "DICT          " "Friulian (north-east Italy)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} fy_NL "DICT          " "Frisian (Netherlands)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ga_IE "DICT HYPH     " "Irish (Ireland)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} gd_GB "DICT          " "Scottish Gaelic (Scotland)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} gl_ES "DICT          " "Galician (Spain)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} gsc_FR "DICT          " "Gascon (France)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} he_IL "DICT          " "Hebrew (Israel)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} hi_IN "DICT          " "Hindi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} hr_HR "DICT          " "Croatian (Croatia)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} hu_HU "DICT HYPH THES" "Hungarian (Hungary)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} hy_AM "DICT          " "Armenian (Eastern and Western)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} id_ID "DICT HYPH     " "Indonesian (Indonesia)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} is_IS "DICT HYPH     " "Icelandic (Iceland)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} it_IT "DICT HYPH THES" "Italian (Italy)" LGPL/GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} km_KH "DICT          " "Khmer (Cambodia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ku_TR "DICT          " "Kurdish (Iran)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} la_LA "DICT          " "Latin (x-register)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} lt_LT "DICT HYPH     " "Lithuanian (Lithuania)" BSD-like 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} lv_LV "DICT          " "Latvian (Latvia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} mg_MG "DICT          " "Malagasy (Madagascar)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} mi_NZ "DICT          " "Maori (New Zealand)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} mn_MN "DICT          " "Mongolian (Mongolia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} mr_IN "DICT          " "Marathi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ms_MY "DICT          " "Malay (Malaysia)" "GNU Free Documentation License" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} nb_NO "DICT          " "Norwegian/Bokmel (Norway)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ne_NP "DICT          " "Nepali (Nepal)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} nl_NL "DICT HYPH     " "Dutch (Netherlands)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} nn_NO "DICT          " "Norwegian/Nynorsk (Norway)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} nr_ZA "DICT          " "Ndebele (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ns_ZA "DICT          " "Northern Sotho (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ny_MW "DICT          " "Chichewa (Malawi)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} oc_FR "DICT          " "Occitan (France)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} or_OR "DICT          " "Oriya (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} pa_PA "DICT          " "Punjabi (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} pl_PL "DICT HYPH THES" "Polish (Poland)" "Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} pt_BR "DICT HYPH     " "Portuguese (Brasil)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} pt_PT "DICT HYPH     " "Portuguese (Portugal)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} qu_BO "DICT          " "Quechua (Bolivia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ro_RO "DICT HYPH     " "Romanian (Romania)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ru_RU "DICT HYPH THES" "Russian (Russia)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} rw_RW "DICT          " "Kinyarwanda (Rwanda)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} sk_SK "DICT HYPH THES" "Slovak (Slovak Republic)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} sl_SI "DICT HYPH     " "Slovenian (Slovenia)" BSD-like 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ss_ZA "DICT          " "Swazi/Swati (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} st_ZA "DICT          " "Southern Sotho (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} sv_SE "DICT HYPH     " "Swedish (Sweden)" GPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} sw_KE "DICT          " "Kiswahili (Africa)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} sw_TZ "DICT          " "Kiswahili (East Africa) Extended Wordlist" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ta_TA "DICT          " "Tamil (India)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} tet_ID "DICT          " "Tetum (Indonesia)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} th_TH "DICT          " "Thai (Thailand)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} tl_PH "DICT          " "Tagalog (Philippines)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} tn_ZA "DICT          " "Setswana (Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ts_ZA "DICT          " "Tsonga (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} uk_UA "DICT HYPH     " "Ukrainian (Ukraine)" LGPL 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} uz_UZ "DICT          " "Uzbek (Uzbekistan)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} ve_ZA "DICT          " "Venda (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} vi_VI "DICT          " "Vietnamese (Vietnam)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} xh_ZA "DICT          " "Xhosa (South Africa)" "Check readme" 2>/dev/null )}
%{expand:%(/bin/sh %{SOURCE0} zu_ZA "DICT          " "Zulu (South Africa)" LGPL 2>/dev/null )}

%prep
%setup -q -T -c

# Handle spelling dictionaries
all_dicts="%{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
		%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
		%{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE116} %{SOURCE117} %{SOURCE118} %{SOURCE119} \
		%{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
		%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} \
		%{SOURCE135} %{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} \
		%{SOURCE140} %{SOURCE141} %{SOURCE142} %{SOURCE143} %{SOURCE144} \
		%{SOURCE145} %{SOURCE146} %{SOURCE147} %{SOURCE148} %{SOURCE149} \
		%{SOURCE150} %{SOURCE151} %{SOURCE152} %{SOURCE153}              \
		%{SOURCE155} %{SOURCE156} %{SOURCE157} %{SOURCE158} %{SOURCE159} \
		%{SOURCE160} %{SOURCE161} %{SOURCE162} %{SOURCE163} %{SOURCE164} \
		%{SOURCE165} %{SOURCE166} %{SOURCE167} %{SOURCE168} %{SOURCE169} \
		%{SOURCE170} %{SOURCE171} %{SOURCE172} %{SOURCE173} %{SOURCE174} \
		%{SOURCE175} %{SOURCE176} %{SOURCE177} %{SOURCE178} %{SOURCE179} \
		%{SOURCE180} %{SOURCE181} %{SOURCE182} %{SOURCE183} %{SOURCE184} \
		%{SOURCE185} %{SOURCE186} %{SOURCE187} %{SOURCE188}              \
		%{SOURCE190} %{SOURCE191} %{SOURCE192} %{SOURCE193}"
for dictfile in $all_dicts
do
  basefile="${dictfile##*/}"
  langpack="${basefile/.zip/}"
  echo "LANGPACK=$langpack"
  mkdir -p doc/DICT/$langpack
  unzip -d doc/DICT/$langpack $dictfile
  mkdir -p dic/DICT/$langpack
  mv doc/DICT/$langpack/$langpack.{aff,dic} dic/DICT/$langpack
  # Protect against #36685
  rm -f doc/DICT/$langpack/*.aff 2> /dev/null
  rm -f doc/DICT/$langpack/*.dic 2> /dev/null
  # create dummy file if docdir is empty
  if ! ls doc/DICT/$langpack/* ; then
cat > doc/DICT/$langpack/README_$langpack.txt << EOF
Spell checking dictionary for $langpack
EOF
  fi
  # fix permissions
  chmod 644 doc/DICT/$langpack/*
  # add symlinks for mozilla apps
  mkdir -p moz
  lang=$(echo $langpack|sed 's/_.*//')
  if [ $(echo $all_dicts |tr ' ' \\n |grep /${lang}_ |wc -l) \> 1 ]; then
    lang=$(echo $langpack |tr _ -)
  fi
  ln -s ../ooo/$langpack.aff moz/$lang.aff
  ln -s ../ooo/$langpack.dic moz/$lang.dic
  echo %{mozdictdir}/$lang.aff > $langpack.files
  echo %{mozdictdir}/$lang.dic >> $langpack.files
done

# Handle spelling dictionaries
for hyphfile in %{SOURCE200} %{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} \
		%{SOURCE205} %{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} \
		%{SOURCE210} %{SOURCE211} %{SOURCE212} %{SOURCE213} %{SOURCE214} \
		%{SOURCE215} %{SOURCE216} %{SOURCE217} %{SOURCE218} %{SOURCE219} \
		%{SOURCE220} %{SOURCE221} %{SOURCE222} %{SOURCE223} %{SOURCE224} \
		%{SOURCE225} %{SOURCE226} %{SOURCE227} %{SOURCE228} %{SOURCE229}
do
  basefile="${hyphfile##*/}"
  langpack="${basefile/.zip/}"
  echo "LANGPACK/(HPY)=$langpack"
  mkdir -p doc/HYPH/$langpack
  unzip -d doc/HYPH/$langpack $hyphfile
  mkdir -p dic/HYPH/$langpack
  mv doc/HYPH/$langpack/$langpack.dic dic/HYPH/$langpack
  # Protect against #36685
  rm -f doc/HYPH/$langpack/*.dic 2> /dev/null
  # create dummy file if docdir is empty
  if ! ls doc/HYPH/$langpack/* ; then
cat > doc/HYPH/$langpack/README_$langpack.txt << EOF
Hyphenation dictionary for $langpack
EOF
  fi
  # fix permissions
  chmod 644 doc/HYPH/$langpack/*
done

# Handle thesaurus dictionaries
for thesfile in %{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} %{SOURCE304} \
		%{SOURCE305} %{SOURCE306} %{SOURCE307}              %{SOURCE309} \
		%{SOURCE310} %{SOURCE311} %{SOURCE312}
do
  basefile="${thesfile##*/}"
  langpack="${basefile/.zip/}"
  echo "LANGPACK(thes)=$langpack"
  mkdir -p doc/THES/$langpack
  unzip -d doc/THES/$langpack $thesfile
  mkdir -p dic/THES/$langpack
  mv doc/THES/$langpack/$langpack.{dat,idx} dic/THES/$langpack
  # Protect against #36685
  rm -f doc/THES/$langpack/*.dat 2> /dev/null
  rm -f doc/THES/$langpack/*.idx 2> /dev/null
  # create dummy file if docdir is empty
  if ! ls doc/THES/$langpack/* ; then
cat > doc/THES/$langpack/README_$langpack.txt << EOF
Thesaurus dictionary for $langpack
EOF
  fi
  # fix permissions
  chmod 644 doc/THES/$langpack/*
done

# protect against #36685
[ -n "$(find doc/ -name '*.dic')" ] && exit 1
[ -n "$(find doc/ -name '*.aff')" ] && exit 1
[ -n "$(find doc/ -name '*.dat')" ] && exit 1
[ -n "$(find doc/ -name '*.idx')" ] && exit 1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{dictdir}/

# Install spell checking dictionaries
for file in dic/DICT/*/*; do
  install -m 644 $file %{buildroot}%{dictdir}/${file##*/}
done

# Install hyphenation dictionaries
for file in dic/HYPH/*/*; do
  install -m 644 $file %{buildroot}%{dictdir}/${file##*/}
done

# Install thesaurus dictionaries
for file in dic/THES/*/*; do
  install -m 644 $file %{buildroot}%{dictdir}/${file##*/}
done

# #42885 
cd %{buildroot}%{dictdir}
for file in *.idx *.dat; do
  ln -s $file `echo $file|sed 's/\(.*\)\.\(idx\|dat\)/\1_v2\.\2/' `
done
ln -s th_en_US.idx th_en_GB_v2.idx
ln -s th_en_US.dat th_en_GB_v2.dat
cd -

# Install the spell checking dictionary symlinks for mozilla apps
mkdir -p %{buildroot}%{mozdictdir}/

for file in moz/*; do
  cp -P $file %{buildroot}%{mozdictdir}/${file##*/}
done

%clean
rm -rf %{buildroot}

%nil
