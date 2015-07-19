# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/icehyph.tex
# catalog-date 2007-04-17 11:56:04 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-hyphen-icelandic
Version:	20070417
Release:	11
Summary:	Icelandic hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/icehyph.tex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-icelandic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Icelandic in T1/EC and UTF-8
encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-icelandic
%_texmf_language_def_d/hyphen-icelandic
%_texmf_language_lua_d/hyphen-icelandic

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-icelandic <<EOF
\%% from hyphen-icelandic:
icelandic loadhyph-is.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-icelandic
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-icelandic <<EOF
\%% from hyphen-icelandic:
\addlanguage{icelandic}{loadhyph-is.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-icelandic
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-icelandic <<EOF
-- from hyphen-icelandic:
	['icelandic'] = {
		loader = 'loadhyph-is.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-is.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070417-3
+ Revision: 767557
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070417-2
+ Revision: 759918
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070417-1
+ Revision: 718660
- texlive-hyphen-icelandic
- texlive-hyphen-icelandic
- texlive-hyphen-icelandic
- texlive-hyphen-icelandic

