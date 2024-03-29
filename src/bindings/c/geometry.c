
#include "geometry.h"

#include "string.h"

void add_mesh_c(const char *AIRWAY_MESHFILE, int *filename_len);
void add_matching_mesh_c();
void append_units_c();
void define_1d_elements_c(const char *ELEMFILE, int *filename_len);
void define_elem_geometry_2d_c(const char *ELEMFILE, int *filename_len, const char *SF_OPTION, int *sf_option_len);
void define_mesh_geometry_test_c();
void define_node_geometry_c(const char *NODEFILE, int *filename_len);
void define_node_geometry_2d_c(const char *NODEFILE, int *filename_len);
void define_data_geometry_c(const char *DATAFILE, int *filename_len);
void group_elem_parent_term_c(int *ne_parent);
void make_data_grid_c(int *surface_elems, double *spacing, int *to_export, const char *filename, int *filename_len, const char *groupname, int *groupname_len);
void define_rad_from_file_c(const char *FIELDFILE, int *filename_len, const char *radius_type, int *radius_type_len);
int get_local_node_f_c(const char *ndimension, int *dimension_len, const char *np_global, int *np_global_len);
void define_rad_from_geom_c(const char *order_system, int *order_system_len, double *control_param,
                            const char *start_from, int *start_from_len, double *start_rad,
                            const char *group_type, int *group_type_len, const char *group_options, int *group_options_len);
void get_terminal_density_from_file_c(const char *DENSITYFILE, int *filename_len, const char *CFILE, int *cfilename_len);
void element_connectivity_1d_c();
void evaluate_ordering_c();
void set_initial_volume_c(int *Gdirn, double *COV, double *total_volume, double *Rmax, double *Rmin);
void set_volume_fromrv_c(const char *UNITFILE, int *filename_len);
void volume_of_mesh_c(double *volume_model, double *volume_tree);
void set_constriction_from_file_c(const char *CNSTCTFILE, int *filename_len);

void add_mesh(const char *AIRWAY_MESHFILE)
{
  int filename_len = strlen(AIRWAY_MESHFILE);
  add_mesh_c(AIRWAY_MESHFILE, &filename_len);
}

void add_matching_mesh()
{
	add_matching_mesh_c();
}

void append_units()
{
  append_units_c();
}

void define_1d_elements(const char *ELEMFILE)
{
  int filename_len = strlen(ELEMFILE);
  define_1d_elements_c(ELEMFILE, &filename_len);
}

void define_elem_geometry_2d(const char *ELEMFILE, const char *SF_OPTION)
{
  int filename_len = strlen(ELEMFILE);
  int sf_option_len = strlen(SF_OPTION);
  define_elem_geometry_2d_c(ELEMFILE, &filename_len, SF_OPTION, &sf_option_len);
}

void define_mesh_geometry_test()
{
  define_mesh_geometry_test_c();
}

void define_node_geometry(const char *NODEFILE)
{
  int filename_len = strlen(NODEFILE);
  define_node_geometry_c(NODEFILE, &filename_len);
}

void define_node_geometry_2d(const char *NODEFILE)
{
  int filename_len = strlen(NODEFILE);
  define_node_geometry_2d_c(NODEFILE, &filename_len);
}

void define_data_geometry(const char *DATAFILE)
{
  int filename_len = strlen(DATAFILE);
  define_data_geometry_c(DATAFILE, &filename_len);
}

void group_elem_parent_term(int ne_parent)
{
  group_elem_parent_term_c(&ne_parent);
}

void make_data_grid(int surface_elems, double spacing, int to_export, const char *filename, const char *groupname)
{
  int filename_len = strlen(filename);
  int groupname_len = strlen(groupname);
  make_data_grid_c(&surface_elems, &spacing, &to_export, filename, &filename_len, groupname, &groupname_len);
}

void define_rad_from_file(const char *FIELDFILE, const char *radius_type)
{
  int filename_len = strlen(FIELDFILE);
  int radius_type_len = strlen(radius_type);
  define_rad_from_file_c(FIELDFILE, &filename_len, radius_type, &radius_type_len);
}

int get_local_node_f(const char *ndimension, const char *np_global)
{
  int dimension_len = strlen(ndimension);
  int np_global_len = strlen(np_global);
  get_local_node_f_c(ndimension, &dimension_len, np_global, &np_global_len);
}

void define_rad_from_geom(const char *order_system, double control_param, const char *start_from,
                          double start_rad, const char*group_type, const char *group_options)
{
  int order_system_len = strlen(order_system);
  int start_from_len = strlen(start_from);
  int group_type_len = strlen(group_type);
  int group_options_len = strlen(group_options);
  define_rad_from_geom_c(order_system, &order_system_len, &control_param, start_from, &start_from_len, &start_rad,
                         group_type, &group_type_len, group_options, &group_options_len);

}

void get_terminal_density_from_file(const char *DENSITYFILE, const char *CFILE)
{
  int filename_len = strlen(DENSITYFILE);
  int cfilename_len = strlen(CFILE);
  get_terminal_density_from_file_c(DENSITYFILE, &filename_len, CFILE, &cfilename_len);
}

void element_connectivity_1d()
{
  element_connectivity_1d_c();
}

void evaluate_ordering()
{
  evaluate_ordering_c();
}

void set_initial_volume(int Gdirn, double COV, double total_volume, double Rmax, double Rmin)
{
  set_initial_volume_c(&Gdirn, &COV, &total_volume, &Rmax, &Rmin);
}

void set_volume_fromrv(const char *UNITFILE)
{
  int filename_len = strlen(UNITFILE);
  set_volume_fromrv_c(UNITFILE, &filename_len);
}

void set_constriction_from_file(const char *CNSTCTFILE)
{
  int filename_len = strlen(CNSTCTFILE);
  set_constriction_from_file_c(CNSTCTFILE, &filename_len);
}

void volume_of_mesh(double *volume_model, double *volume_tree)
{
  volume_of_mesh_c(volume_model, volume_tree);
}
