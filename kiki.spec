Summary:	kiki the nano bot is a 3-D puzzle game
Summary(pl):	kiki the nano bot jest trójwymiarow± gr± logiczn±
Name:		kiki
Version:	0.9.0
Release:	2
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
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	swig
BuildRequires:	glut-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kiki the nano bot is a 3-D puzzle game, basically a mixture of the games
Sokoban and Kula-World. 
     
%description -l pl
kiki the nano bot jest trójwymiarow± gr±, opart± na mieszance gier Sokoban oraz
Kula-World. 

%prep
%setup -q -n %{name}_src
%patch0 -p1

%build
cd kodilib/linux

%{__make} \
	CXX="%{__cxx}" \
	SDL_CFLAGS="%{rpmcflags} -D_REENTRANT" \
	X11INCLUDES="-I/usr/X11R6/include"

cd ../../kiki/linux

# try to detect python version
PYTHON_VER=""
[ -d "/usr/include/python2.2" ] && PYTHON_VER="2.2"
[ -d "/usr/include/python2.3" ] && PYTHON_VER="2.3"
[ "$PYTHON_VER" == "" ] && \
    echo "Unknown python version or python-devel not found!" \
    exit 1

%{__make} \
	CXX="%{__cxx}" \
	SDL_CFLAGS="%{rpmcflags} -D_REENTRANT" \
	X11_INCLUDES="-I/usr/X11R6/include" \
	GLLIBS="-L/usr/X11R6/lib -lglut -lGLU -lGL" \
	PYTHON_VERSION=$PYTHON_VER \
	PYTHONLIBS="\
	    /usr/lib/libpython$PYTHON_VER.so* -lutil \
            /usr/lib/python$PYTHON_VER/lib-dynload/math.so \
	    /usr/lib/python$PYTHON_VER/lib-dynload/time.so"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{py,sounds}

install kiki/linux/kiki $RPM_BUILD_ROOT%{_bindir}
install kiki/py/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/py
install kiki/py/*.cfg $RPM_BUILD_ROOT%{_datadir}/%{name}/py
install kiki/py/*.hsc $RPM_BUILD_ROOT%{_datadir}/%{name}/py
install kiki/py/*.rec $RPM_BUILD_ROOT%{_datadir}/%{name}/py
install kiki/sounds/*.{wav,mp3,aif{,f}} $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc kiki/{Readme.txt,Thanks.txt}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
