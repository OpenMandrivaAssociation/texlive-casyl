# revision 15878
# category Package
# catalog-ctan /language/casyl
# catalog-date 2008-10-26 18:17:50 +0100
# catalog-license pd
# catalog-version 2.0
Name:		texlive-casyl
Version:	2.0
Release:	8
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

%description
The bundle constitutes a font (as MetaFont source) and LaTeX
macros for its use within a document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 749979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718011
- texlive-casyl
- texlive-casyl
- texlive-casyl
- texlive-casyl
- texlive-casyl

