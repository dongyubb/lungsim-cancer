
%module(package="aether") geometry
%include symbol_export.h

%{
#include "geometry.h"
%}

// define_rad_from_file has an optional argument that C cannot replicate,
// so we use SWIG to override with a C++ version that can.
void define_rad_from_file(const char *FIELDFILE, const char *radius_type="no_taper");
void define_rad_from_geom(const char *ORDER_SYSTEM, double CONTROL_PARAM, const char *START_FROM, double START_RAD, const char *group_type_in="all", const char *group_option_in="dummy");
void get_terminal_density_from_file(const char *DENSITYFILE,const char *CFILE);
void set_volume_fromrv(const char *UNITFILE);
void set_constriction_from_file(const char *CNSTCTFILE);

%include geometry.h

