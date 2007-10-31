%define dictdir	%{_datadir}/dict/ooo

Summary:	MySpell Spelling and Hyphenation dictionaries
Name:		myspell-dictionaries
Version:	1.0.2
Release:	%mkrel 12
URL:		http://lingucomponent.openoffice.org/download_dictionary.html
Source0:	myspell-genpackages.sh
License:	BSD/GPL/LGPL
Group:		System/Internationalization
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	unzip

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

# From http://www.kurnik.pl/dictionary/alt-myspell-pl-20040816.tar.bz2
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

##
## Packages information
##

%description
myspell-* packages contain spell checking data to be used by
OpenOffice.org or any other MySpell-capable application, like
Mozilla. myspell-hyph-* packages contain hyphenation dictionaries for
a particular set of languages.

# Spelling dictionaries
%{expand:%(/bin/sh %{SOURCE0} DESC DICT af_ZA "Afrikaans (Africa)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT bg_BG "Bulgarian (Bulgaria)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ca_ES "Catalan" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT cs_CZ "Czech (Czech Republic)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT cy_GB "Welsh (Wales)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT da_DK "Danish (Denmark)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_AT "German (Austria)"  GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_CH "German (Switzerland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_DE "German (Germany)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT el_GR "Greek (Greece)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_AU "English (Australian)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_CA "English (Canada)" "Public Domain" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_GB "English (United Kingdom)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_NZ "English (New Zealand)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_US "English (US)" BSD 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT es_ES "Spanish (Spain)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT es_MX "Spanish (Mexico)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT et_EE "Estonian (Estonia)" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT fo_FO "Faroese (Faroe Islands)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT fr_FR "French (France)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ga_IE "Irish (Ireland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT gl_ES "Galician (Spain)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT hr_HR "Croatian (Croatia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT hu_HU "Hungarian (Hungary)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT id_ID "Indonesian (Indonesia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT it_IT "Italian (Italy)" LGPL/GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT lt_LT "Lithuanian (Lithuania)" BSD-like 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT mi_NZ "Maori (New Zealand)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ms_MY "Malay (Malaysia)" "GNU Free Documentation License" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nb_NO "Norwegian/Bokmål (Norway)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nl_NL "Dutch (Netherlands)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nn_NO "Norwegian/Nynorsk (Norway)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pl_PL "Polish (Poland)" "Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pt_BR "Portuguese (Brasil)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pt_PT "Portuguese (Portugal)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ro_RO "Romanian (Romania)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ru_RU "Russian (Russia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sk_SK "Slovak (Slovak Republic)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sl_SI "Slovenian (Slovenia)" BSD-like 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sv_SE "Swedish (Sweden)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sw_KE "Kiswahili (Africa)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT uk_UA "Ukrainian (Ukraine)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT zu_ZA "Zulu (South Africa)" LGPL 2>/dev/null)}

# Hyphenation
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH bg_BG "Bulgarian" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH cs_CZ "Czech" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH da_DK "Danish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH de_CH "German" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH de_DE "German" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH el_GR "Greek" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH en_CA "English" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH en_GB "English" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH en_US "English" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH es_ES "Spanish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH et_EE "Estonian" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH fi_FI "Finnish" "freely distributable" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH fr_BE "French" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH fr_FR "French" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH ga_IE "Irish" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH hu_HU "Hungarian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH id_ID "Indonesian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH is_IS "Icelandic" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH it_IT "Italian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH lt_LT "Lithuanian" LPPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH nl_NL "Dutch" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH pl_PL "Polish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH pt_BR "Brazilian Portuguese" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH pt_PT "Portuguese" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH ro_RO "Romanian (Romania)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH ru_RU "Russian" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sk_SK "Slovak" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sl_SI "Slovenian" "Copyright Matjaz Vrecko" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sv_SE "Swedish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH uk_UA "Ukrainian" GPL 2>/dev/null)}

# Thesaurus
%{expand:%(/bin/sh %{SOURCE0} DESC THES bg_BG "Bulgarian (Bulgaria)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES de_DE "German (Germany)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES en_US "English (US)" BSD 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES es_ES "Spanish (Spain)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES fr_FR "French (France)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES it_IT "Italian (Italy)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES pl_PL "Polish (Poland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES sk_SK "Slovak (Slovak Republic)" GPL 2>/dev/null)}

%prep
%setup -q -T -c

# Handle spelling dictionaries
for dictfile in %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
		%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
		%{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE116} %{SOURCE117} %{SOURCE118} %{SOURCE119} \
		%{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
		%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} \
		%{SOURCE135} %{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} \
		%{SOURCE140} %{SOURCE141} %{SOURCE142}
do
  basefile="${dictfile##*/}"
  langpack="${basefile/.zip/}"
  echo "LANGPACK=$langpack"
  mkdir -p doc/DICT/$langpack
  unzip -d doc/DICT/$langpack $dictfile
  mkdir -p dic/DICT/$langpack
  mv doc/DICT/$langpack/$langpack.{aff,dic} dic/DICT/$langpack
  # create dummy file if docdir is empty
  if ! ls doc/DICT/$langpack/* ; then
cat > doc/DICT/$langpack/README_$langpack.txt << EOF
Spell checking dictionary for $langpack
EOF
  fi
  # fix permissions
  chmod 644 doc/DICT/$langpack/*
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
		%{SOURCE305} %{SOURCE306} %{SOURCE307}
do
  basefile="${thesfile##*/}"
  langpack="${basefile/.zip/}"
  echo "LANGPACK(thes)=$langpack"
  mkdir -p doc/THES/$langpack
  unzip -d doc/THES/$langpack $thesfile
  mkdir -p dic/THES/$langpack
  mv doc/THES/$langpack/$langpack.{dat,idx} dic/THES/$langpack
  # create dummy file if docdir is empty
  if ! ls doc/THES/$langpack/* ; then
cat > doc/THES/$langpack/README_$langpack.txt << EOF
Thesaurus dictionary for $langpack
EOF
  fi
  # fix permissions
  chmod 644 doc/THES/$langpack/*
done

%build

%install
rm -rf %buildroot
mkdir -p %buildroot%{dictdir}/

# Install spell checking dictionaries
for file in dic/DICT/*/*; do
  install -m 644 $file %buildroot%{dictdir}/${file##*/}
done

# Install hyphenation dictionaries
for file in dic/HYPH/*/*; do
  install -m 644 $file %buildroot%{dictdir}/${file##*/}
done

# Install thesaurus dictionaries
for file in dic/THES/*/*; do
  install -m 644 $file %buildroot%{dictdir}/${file##*/}
done

%clean
rm -rf %buildroot

##
## Scripts for spell checking
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT af ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT bg BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ca ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT cs CZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT cy GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT da DK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de AT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de CH 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT el GR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en "GB ZA ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en AU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en CA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT es "MX AR CO" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT es ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT et EE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT fo FO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT fr "FR BE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ga IE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT gl ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT hr HR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT hu HU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT id ID 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT it IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT lt LT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT mi NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ms MY 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nb NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nl NL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nn NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pl PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pt BR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pt PT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ro RO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ru RU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sk SK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sl SI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sv SE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sw KE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT uk UA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT zu ZA 2>/dev/null)}

##
## Scripts for hyphenation
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH bg_BG "BG" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH cs_CZ "CZ" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH da_DK "DA"  2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH de_CH "CH" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH de_DE "DE AT LI LU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH el_GR "GR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH en_CA "CA" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH en_GB "GB" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH en_US "US NZ AU ZA IE JM PH TT ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH es_ES "ES AR BZ BO CL CO CR CU DO EC SV GU JN MX NI PA PU PE PR UY VE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH et_EE "EE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH fi_FI "FI" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH fr_BE "BE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH fr_FR "FR CA LU MC CH" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH ga_IE "IE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH hu_HU "HU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH id_ID "ID" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH is_IS "IS" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH it_IT "IT CH" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH lt_LT "LT" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH nl_NL "NL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH pl_PL "PL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH pt_BR "BR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH pt_PT "PT" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH ro_RO "RO" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH ru_RU "RU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sk_SK "SK" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sl_SI "SI" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sv_SE "SE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH uk_UA "UA" 2>/dev/null)}

##
## Scripts for thesaurus
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES bg_BG "BG" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES de_DE "DE AT CH LI LU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES en_US "US CA GB AU BZ IE JM NZ PH TT ZA ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES es_ES "ES AR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES fr_FR "FR BE CA CH LU MC" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES it_IT "IT" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES pl_PL "PL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES sk_SK "SK" 2>/dev/null)}

##
## Files for spell checking
##
%{expand:%(/bin/sh %{SOURCE0} FILES DICT af_ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT bg_BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ca_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT cs_CZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT cy_GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT da_DK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_AT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_CH 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT el_GR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_AU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_CA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT es_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT es_MX 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT et_EE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT fo_FO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT fr_FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ga_IE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT gl_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT hr_HR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT hu_HU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT id_ID 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT it_IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT lt_LT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT mi_NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ms_MY 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nb_NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nl_NL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nn_NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pl_PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pt_BR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pt_PT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ro_RO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ru_RU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sk_SK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sl_SI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sv_SE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sw_KE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT uk_UA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT zu_ZA 2>/dev/null)}

##
## Files for hyphenation
##

%{expand:%(/bin/sh %{SOURCE0} FILES HYPH bg_BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH cs_CZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH da_DK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH de_CH 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH de_DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH el_GR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH en_CA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH en_GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH en_US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH es_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH et_EE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH fi_FI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH fr_BE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH fr_FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH ga_IE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH hu_HU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH id_ID 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH is_IS 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH it_IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH lt_LT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH nl_NL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH pl_PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH pt_BR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH pt_PT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH ro_RO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH ru_RU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sk_SK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sl_SI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sv_SE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH uk_UA 2>/dev/null)}

#
# Files for thesaurus
#
%{expand:%(/bin/sh %{SOURCE0} FILES THES bg_BG BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES de_DE DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES en_US US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES es_ES ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES fr_FR FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES it_IT IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES pl_PL PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES sk_SK SK 2>/dev/null)}
%nil


