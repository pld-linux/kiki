Summary:	kiki the nano bot is a 3-D puzzle game
Summary(pl):	kiki the nano bot jest trójwymiarow± gr± logiczn±
Name:		kiki
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Aplications
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/kiki/%{name}-src-%{version}.tgz
# Source0-md5:	60ec6bdf0196c9c934f683d3bf7a12ea
URL:		http://kiki.sourceforge.net/
Patch0:		kiki-sysconfdir.patch
Requires:	python
Requires:	SDL_mixer
Requires:	SDL_image
Requires:	SDL
BuildRequires:	python
BuildRequires:	swig
#BuildRequires:	swig-python
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
%patch0 -p1

%build
cd kodilib/linux
make
cd ../..
cd kiki/linux

# Yep... thats nasty...

cat Makefile |sed -e s,PYTHON_VERSION=2.2,PYTHON_VERSION=2.3,g > Makefile.pld
cat Makefile.pld |sed -e s,$\(PYTHONHOME\)/config/libpython$\(PYTHON_VERSION\).a,/usr/lib/libpython$\(PYTHON_VERSION\).a,g > Makefile
cat Makefile | sed -e s,/X11/,/X11R6/,g > Makefile.pld
mv Makefile.pld Makefile
make
cd ../..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/py
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sounds

install kiki/py/*.py $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/py
install kiki/sounds/*.wav $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sounds
install kiki/sounds/*.mp3 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sounds
install kiki/sounds/*.aiff $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sounds
install kiki/sounds/*.aif $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sounds


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc kiki/linux/Readme.txt 
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}/py/*
%{_sysconfdir}/%{name}/sounds/*
