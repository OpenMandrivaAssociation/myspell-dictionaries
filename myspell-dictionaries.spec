%define name      myspell-dictionaries
# Define to "1.0" for OOo < 1.0.1
%define myversion 1.0.2
%define myrelease %mkrel 12

%if "%{version}" == "1.0"
%define dictdir	%{_libdir}/myspell
%else
%define dictdir	%{_datadir}/dict/ooo
%endif

Summary:	MySpell Spelling and Hyphenation dictionaries
Name:		%{name}
Version:	%{myversion}
Release:	%{myrelease}
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
Source132: fr_BE.zip
Source133: lt_LT.zip

Source134: ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/et_EE.zip

# http://sourceforge.net/project/showfiles.php?group_id=91920
Source135: af_ZA.zip

Source136: cy_GB.zip
Source137: en_NZ.zip
Source138: id_ID.zip
Source139: zu_ZA.zip
Source140: ro_RO.zip
Source141: mi_NZ.zip
Source142: sw_KE.zip
Source143: ms_MY.zip

##
## Sources for hyphenation dictionaries
##

Source200: hyph_da.zip
Source201: hyph_en.zip
Source202: hyph_fr.zip
Source203: hyph_de.zip
Source204: hyph_it.zip
Source205: hyph_ru.zip
Source206: hyph_nl.zip
Source207: hyph_cs.zip
Source208: hyph_es.zip
Source209: hyph_sk.zip
Source210: hyph_sl.zip
Source211: hyph_uk.zip
Source212: hyph_hu.zip
Source213: hyph_sv.zip
Source214: ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/hyph_et.zip
Source215: hyph_id.zip
Source216: hyph_pl.zip
Source217: hyph_pt.zip
Source218: hyph_el.zip
# See http://bgoffice.sourceforge.net/ooo/index.html (http://heanet.dl.sourceforge.net/sourceforge/bgoffice/OOo-hyph-bg-4.0.zip)
Source219: hyph_bg.zip
Source220: hyph_lt.zip
Source221: hyph_is.zip
Source222: hyph_ga.zip
Source223: hyph_fi.zip

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
%{expand:%(/bin/sh %{SOURCE0} DESC DICT bg_BG 20040402 "Bulgarian (Bulgaria)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ca_ES 20030907 "Catalan" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT hr_HR 20020411 "Croatian (Croatia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT cs_CZ 20030907 "Czech (Czech Republic)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT da_DK 20040609 "Danish (Denmark)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nl_NL 20070606 "Dutch (Netherlands)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_CA 20020315 "English (Canada)" "Public Domain" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_GB 20040208 "English (United Kingdom)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_US 20040623 "English (US)" BSD 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT fr_FR 20020608 "French (France)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_DE 20030905 "German (Germany)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_CH 20030905 "German (Switzerland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT el_GR 20040424 "Greek (Greece)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT hu_HU 20040331 "Hungarian (Hungary)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT it_IT 20050521 "Italian (Italy)" LGPL/GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pl_PL 20040816 "Polish (Poland)" "Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pt_PT 20020629 "Portuguese (Portugal)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT pt_BR 20030110 "Portuguese (Brasil)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT es_ES 20040626 "Spanish (Spain)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sk_SK 20040118 "Slovak (Slovak Republic)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sv_SE 20030814 "Swedish (Sweden)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nb_NO 20031013 "Norwegian/Bokmål (Norway)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT nn_NO 20031013 "Norwegian/Nynorsk (Norway)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ga_IE 20040404 "Irish (Ireland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT gl_ES 20030905 "Galician (Spain)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ru_RU 20040406 "Russian (Russia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sl_SI 20030907 "Slovenian (Slovenia)" BSD-like 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT uk_UA 20070529 "Ukrainian (Ukraine)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT de_AT 20030905 "German (Austria)"  GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_AU 20030329 "English (Australian)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT es_MX 20030818 "Spanish (Mexico)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT fo_FO 20040403 "Faroese (Faroe Islands)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT fr_BE 20030619 "French (Belgium)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT lt_LT 20031231 "Lithuanian (Lithuania)" BSD-like 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT et_EE 20040621 "Estonian (Estonia)" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT af_ZA 20040727 "Afrikaans (Africa)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT cy_GB 20040425 "Welsh (Wales)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT en_NZ 20030907 "English (New Zealand)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT id_ID 20040810 "Indonesian (Indonesia)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT zu_ZA 20040604 "Zulu (South Africa)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ro_RO 20031023 "Romanian (Romania)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT mi_NZ 20030909 "Maori (New Zealand)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT sw_KE 20040516 "Kiswahili (Africa)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC DICT ms_MY 20040907 "Malay (Malaysia)" "GNU Free Documentation License" 2>/dev/null)}

# Hyphenation
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH da 20020727 "Danish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH en 20020727 "English" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH fr 20020727 "French" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH de 20020727 "German" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH it 20030904 "Italian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH ru 20020727 "Russian" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH nl 20041001 "Dutch" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH cs 20030101 "Czech" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH es 20040602 "Spanish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sk 20030101 "Slovak" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sl 20021003 "Slovenian" "Copyright Matjaz Vrecko" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH uk 20021219 "Ukrainian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH hu 20031107 "Hungarian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH sv 20030814 "Swedish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH et 20040621 "Estonian" "free, see http://www.eki.ee/eki/licence.html" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH id 20040810 "Indonesian" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH pl 20030913 "Polish" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH pt 20030904 "Portuguese" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH el 20040409 "Greek" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH bg 20040417 "Bulgarian" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH lt 20040111 "Lithuanian" LPPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH is 20030918 "Icelandic" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH ga 20040212 "Irish" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC HYPH fi 20031125 "Finnish" "freely distributable" 2>/dev/null)}

# Thesaurus
%{expand:%(/bin/sh %{SOURCE0} DESC THES en_US 20040423 "English (US)" BSD 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES fr_FR 20030819 "French (France)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES it_IT 20060812 "Italian (Italy)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES de_DE 20040702 "German (Germany)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES es_ES 20040712 "Spanish (Spain)" LGPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES pl_PL 20040803 "Polish (Poland)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES bg_BG 20040402 "Bulgarian (Bulgaria)" GPL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} DESC THES sk_SK 20050218 "Slovak (Slovak Republic)" GPL 2>/dev/null)}

%prep
%setup -q -n %{name}-%{myversion}-%{myrelease} -T -c

# Handle spelling dictionaries
for dictfile in %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
		%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
		%{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE116} %{SOURCE117} %{SOURCE118} %{SOURCE119} \
		%{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
		%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} \
		%{SOURCE135} %{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} \
		%{SOURCE140} %{SOURCE141} %{SOURCE142} %{SOURCE143}
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
		%{SOURCE220} %{SOURCE221} %{SOURCE222} %{SOURCE223}
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{dictdir}/

# Install spell checking dictionaries
for file in dic/DICT/*/*; do
  install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install hyphenation dictionaries
for file in dic/HYPH/*/*; do
  install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install thesaurus dictionaries
for file in dic/THES/*/*; do
  install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

%clean
rm -rf $RPM_BUILD_ROOT

##
## Scripts for spell checking
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT bg BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ca ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT hr HR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT cs CZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT da DK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nl NL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en CA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en "GB ZA ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT fr FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de CH 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT el GR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT hu HU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT it IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pl PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pt PT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT pt BR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT es ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sk SK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sv SE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nb NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT nn NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ga IE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT gl ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ru RU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sl SI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT uk UA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT de AT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en AU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT es "MX AR CO" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT fo FO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT fr BE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT lt LT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT et EE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT af ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT cy GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT en NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT id ID 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT zu ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ro RO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT mi NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT sw KE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS DICT ms MY 2>/dev/null)}

##
## Scripts for hyphenation
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH da "DA"  2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH en "US CA GB NZ AU ZA IE JM PH TT ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH fr "FR BE CA LU MC CH" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH de "DE AT CH LI LU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH it "IT CH" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH ru "RU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH nl "NL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH cs "CZ" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH es "ES AR BZ BO CL CO CR CU DO EC SV GU JN MX NI PA PU PE PR UY VE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sk "SK" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sl "SI" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH uk "UA" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH hu "HU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH sv "SE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH et "EE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH id "ID" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH pl "PL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH pt "PT BR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH el "GR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH bg "BG" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH lt "LT" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH is "IS" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH ga "IE" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS HYPH fi "FI" 2>/dev/null)}

##
## Scripts for thesaurus
##
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES en_US "US CA GB AU BZ IE JM NZ PH TT ZA ZW" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES fr_FR "FR BE CA CH LU MC" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES it_IT "IT" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES de_DE "DE AT CH LI LU" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES es_ES "ES AR" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES pl_PL "PL" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES bg_BG "BG" 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} SCRIPTS THES sk_SK "SK" 2>/dev/null)}

##
## Files for spell checking
##
%{expand:%(/bin/sh %{SOURCE0} FILES DICT bg_BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ca_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT hr_HR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT cs_CZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT da_DK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nl_NL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_CA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT fr_FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_CH 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT el_GR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT hu_HU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT it_IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pl_PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pt_PT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT pt_BR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT es_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sk_SK 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sv_SE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nb_NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT nn_NO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ga_IE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT gl_ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ru_RU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sl_SI 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT uk_UA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT de_AT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_AU 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT es_MX 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT fo_FO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT fr_BE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT lt_LT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT et_EE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT af_ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT cy_GB 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT en_NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT id_ID 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT zu_ZA 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ro_RO 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT mi_NZ 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT sw_KE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES DICT ms_MY 2>/dev/null)}

##
## Files for hyphenation
##

%{expand:%(/bin/sh %{SOURCE0} FILES HYPH da 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH en 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH fr 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH de 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH it 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH ru 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH nl 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH cs 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH es 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sk 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sl 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH uk 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH hu 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH sv 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH et 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH id 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH pl 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH pt 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH el 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH bg 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH lt 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH is 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH ga 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES HYPH fi 2>/dev/null)}

#
# Files for thesaurus
#
%{expand:%(/bin/sh %{SOURCE0} FILES THES en_US US 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES fr_FR FR 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES it_IT IT 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES de_DE DE 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES es_ES ES 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES pl_PL PL 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES bg_BG BG 2>/dev/null)}
%{expand:%(/bin/sh %{SOURCE0} FILES THES sk_SK SK 2>/dev/null)}
%nil


