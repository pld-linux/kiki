Summary:	kiki the nano bot is a 3-D puzzle game
Summary(pl):	kiki the nano bot - trójwymiarowa gra logiczna
Name:		kiki
Version:	0.9.0
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kiki/%{name}-src-%{version}.tgz
# Source0-md5:	60ec6bdf0196c9c934f683d3bf7a12ea
URL:		http://kiki.sourceforge.net/
Patch0:		%{name}-sysconfdir.patch
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	swig
BuildRequires:	glut-devel
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kiki the nano bot is a 3-D puzzle game, basically a mixture of the
games Sokoban and Kula-World.

%description -l pl
kiki the nano bot jest trójwymiarow± gr±, opart± na mieszance gier
Sokoban oraz Kula-World.

%prep
%setup -q -n %{name}_src
%patch0 -p1

%build
cd kodilib/linux

%{__make} \
	CXX="%{__cxx}" \
	SDL_CFLAGS="%{rpmcflags} -D_REENTRANT" \
	X11INCLUDES="-I/usr/X11R6/include" \
	PYTHONHOME=%{py_libdir}

cd ../../kiki/linux

%{__make} \
	CXX="%{__cxx}" \
	X11_INCLUDES="%{rpmcflags} -I/usr/X11R6/include" \
	GLLIBS="-L/usr/X11R6/%{_lib} -lglut -lGLU -lGL" \
	PYTHONHOME=%{py_libdir} \
	PYTHON_VERSION=%{py_ver} \
	PYTHONLIBS="\
	    /usr/%{_lib}/libpython$PYTHON_VER.so* -lutil \
            %{py_dyndir}/math.so \
	    %{py_dyndir}/time.so"

%install
rm -rf $RPM_BUILD_ROOT
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
