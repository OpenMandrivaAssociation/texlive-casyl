Name:		texlive-casyl
Version:	2.0
Release:	1
Summary:	Typeset Cree/Inuktitut in Canadian Aboriginal Syllabics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/casyl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/casyl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/casyl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle constitutes a font (as MetaFont source) and LaTeX
macros for its use within a document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/casyl/casyll10.mf
%{_texmfdistdir}/fonts/tfm/public/casyl/casyll10.tfm
%{_texmfdistdir}/tex/latex/casyl/casyltex.sty
%doc %{_texmfdistdir}/doc/latex/casyl/README
%doc %{_texmfdistdir}/doc/latex/casyl/casyldoc.pdf
%doc %{_texmfdistdir}/doc/latex/casyl/casyldoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
