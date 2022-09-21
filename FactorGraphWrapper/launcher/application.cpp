
#include "factor_graph_handler.h"

void SLAMTest(FactorGraphHandler& fgh)
{
   using namespace gtsam;

   Pose3 init_pose(Rot3::Ypr(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0));
   fgh.AddPriorPoseFactor(1, init_pose);

   Pose3 odometry(Rot3::Ypr(0.0, 0.0, 0.0), Point3(1.0, 0.0, 0.0));
   fgh.AddOdometryFactor(odometry, 2);

   fgh.OptimizeISAM2(3);

}

int main()
{
    FactorGraphHandler fgh;

    fgh.GetResults().print();

    
}