%global module ordereddict
%define mod %(m=%{module}; echo ${m:0:1})

Summary:	A drop-in substitute for Py2.7's new collections.OrderedDict
Name:		python-%{module}
Version:	1.1
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://pypi.org/project/%{module}/
Source0:	https://files.pythonhosted.org/packages/source/%{mod}/ino/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A drop-in substitute for Py2.7's new collections.OrderedDict.  The recipe has
big-oh performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n) iteration/repr/copy/equality_testing).

Originally based on http://code.activestate.com/recipes/576693/

%files
%{py_sitedir}/ordereddict.py
%{py_sitedir}/ordereddict-*.*-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

