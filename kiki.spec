Summary:	kiki the nano bot is a 3-D puzzle game
Summary(pl):	kiki the nano bot jest trójwymiarow± gr± logiczn±
Name:		kiki
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Aplications
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/kiki/%{name}-src-%{version}.tgz
URL:		http://kiki.sourceforge.net/
Requires:	python
Requires:	SDL_mixer
Requires:	SDL_image
Requires:	SDL
BuildRequires:	python
BuildRequires:	glut-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kiki the nano bot is a 3-D puzzle game, basically a mixture of the games Sokoban 
and Kula-World. 
     
%description -l pl
kiki the nano bot jest trójwymiarow± gr±, opart± na mieszance gier Sokoban oraz
Kula-World. 

%prep
%setup -q -n %{name}_src

%build
cd kodilib/linux
make
cd ../..
cd kiki/linux
make
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  
%{_sysconfdir}/luci/system/users/*
%{_libdir}/%{name}/*
%defattr(755,root,root)
%attr(755,root,root) %{_bindir}/*
