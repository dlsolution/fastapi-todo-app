PAGINATION_DEFAULT_PAGE_SIZE = 10
JSON_FILE_PATH = 'input_file'

STATUS_ACTIVE = 'ACTIVE'
STATUS_DISABLE = 'DISABLE'
MEMBER_ROLE = 'member'
ADMIN_ROLE = 'admin'

SIMULATOR_SUBMITTED_STATUS = 'SUBMITTED'
SIMULATOR_RUNNING_STATUS = 'RUNNING'
SIMULATOR_FAILED_STATUS = 'FAILED'
SIMULATOR_SUCCEEDED_STATUS = 'SUCCEEDED'

ERROR_ID_BAD_REQUEST = 'SYS-0400'
ERROR_ID_UNAUTHENTICATED = 'SYS-0401'
ERROR_ID_FORBIDDEN = 'SYS-0403'
ERROR_ID_NOT_FOUND = 'SYS-0404'
ERROR_ID_SERVER_ERROR = 'SYS-0500'
ERROR_ID_UNKNOWN = 'SYS-0500'
ERROR_ID_RESOURCE_NOT_FOUND = 'RES-0404'
ERROR_ID_VALIDATION_REQUIRED = 'VAL-0001'
ERROR_ID_VALIDATION_WRONG_TYPE = 'VAL-0002'
ERROR_ID_VALIDATION_IN_ENUM = 'VAL-0003'
ERROR_ID_VALIDATION_WRONG_FORMAT = 'VAL-0004'

ERROR_NOT_FOUND = 'Not found'

MATLAB_GEODETIC_CSV = "logPosVel_geod.csv"

GRAFANA_WORKSPACE_CSV = "workspace.csv"
GRAFANA_ATTACK_ANGLE_CSV = "attack_angle.csv"
GRAFANA_DOWN_RANGE_CSV = "down_range.csv"
GRAFANA_GEODETIC_CSV = "pos_vel_geod.csv"

SIMULATOR_DASHBOARD_MAIN_TYPE = "main.m"

SIMULATOR_DASHBOARD_MULTIPLE_OPTIMIZATION_TYPE = "multipleOptimization.m"
OPTIMIZATION_RESULT_CSV = "optimization_result.csv"
PIVOT_OPTIMIZATION_RESULT_CSV = "pivot_optimization_result.csv"
VELOCITY_INTERSECTION_CSV = "velocity_intersection.csv"
PIVOT_VELOCITY_INTERSECTION_CSV = "pivot_velocity_intersection.csv"

OPT_DASHBOARD_STATUS_IN_PROGRESS = "in_progress"
OPT_DASHBOARD_STATUS_SUCCESSFUL = "successful"
OPT_DASHBOARD_STATUS_FAILED = "failed"

REQUEST_HISTORY_STATUS_IN_PROGRESS = "in_progress"
REQUEST_HISTORY_STATUS_SUCCEEDED = "succeeded"
REQUEST_HISTORY_STATUS_FAILED = "failed"

GRAFANA_DASHBOARD_URI = "/api/dashboards/db"

TEST_ANALYSIS = "test_analysis"
WIND_TUNNEL_RESULT = 'wind_tunnel_result'

TEST_ANALYSIS_STATUS_STARTING = "STARTING"
TEST_ANALYSIS_STATUS_SUBMITTED = "SUBMITTED"
TEST_ANALYSIS_STATUS_SUCCEEDED = "SUCCEEDED"
TEST_ANALYSIS_STATUS_FAILED = "FAILED"

TEST_ANALYSIS_DASHBOARD_STATUS_RUNNING = "RUNNING"
TEST_ANALYSIS_DASHBOARD_STATUS_FAILED = "FAILED"
TEST_ANALYSIS_DASHBOARD_STATUS_SUCCEEDED = "SUCCEEDED"
WIND_TUNNEL_RESULT_CSV_NAME = "result.csv"

BATCH_JOB_SUBMITTED_STATUS = 'SUBMITTED'
BATCH_JOB_PENDING_STATUS = 'PENDING'
BATCH_JOB_RUNNABLE_STATUS = 'RUNNABLE'
BATCH_JOB_STARTING_STATUS = 'STARTING'
BATCH_JOB_RUNNING_STATUS = 'RUNNING'
BATCH_JOB_SUCCEEDED_STATUS = 'SUCCEEDED'
BATCH_JOB_FAILED_STATUS = 'FAILED'

TYPE_RAW_DATA = "raw_data"
TYPE_AERODYNAMIC_COEFFICIENTS_DATA = 'aerodynamic_coefficients_data'
