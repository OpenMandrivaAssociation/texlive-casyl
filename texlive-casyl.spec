Name:		texlive-casyl
Version:	15878
Release:	2
Summary:	Typeset Cree/Inuktitut in Canadian Aboriginal Syllabics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/casyl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/casyl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/casyl.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
