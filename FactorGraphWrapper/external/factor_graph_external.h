#pragma once

#include "factor_graph_handler.h"

class FactorGraphExternal
{
    public:
        void AddPriorPoseFactor_Pose3(int index, float* pose);

        void AddOdometryFactor_Pose3(float* odometry, int poseId);

        void AddOrientedPlaneFactor_Vector4(float* lmMean, int lmId, int poseIndex);

        void Optimize();

        void OptimizeISAM2(uint8_t numberOfUpdates);

        void ClearISAM2();

        void SetPoseInitialValue_Pose3(int index, float* value);

        void SetOrientedPlaneInitialValue_OrientedPlane3(int landmarkId, float* value);

        void CreateOdometryNoiseModel_Vector6(float* odomVariance);

        void CreateOrientedPlaneNoiseModel_Vector3(float* lmVariances);

    private:
        FactorGraphHandler fgh;
};