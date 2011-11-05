# revision 15878
# category Package
# catalog-ctan /language/casyl
# catalog-date 2008-10-26 18:17:50 +0100
# catalog-license pd
# catalog-version 2.0
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/casyl/casyll10.mf
%{_texmfdistdir}/fonts/tfm/public/casyl/casyll10.tfm
%{_texmfdistdir}/tex/latex/casyl/casyltex.sty
%doc %{_texmfdistdir}/doc/latex/casyl/README
%doc %{_texmfdistdir}/doc/latex/casyl/casyldoc.pdf
%doc %{_texmfdistdir}/doc/latex/casyl/casyldoc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
