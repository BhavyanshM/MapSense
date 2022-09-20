#pragma once

#include "factor_graph/factor_graph_handler.h"

class FactorGraphExternal
{
    public:
        void AddPriorPoseFactor(int index, float* pose);

        void AddOdometryFactor(gtsam::Pose3 odometry, int poseId);

        void AddOrientedPlaneFactor(gtsam::Vector4 lmMean, int lmId, int poseIndex);

        void optimize();

        void OptimizeISAM2(uint8_t numberOfUpdates);

        void ClearISAM2();

        void SetPoseInitialValue(int index, gtsam::Pose3 value);

        void SetOrientedPlaneInitialValue(int landmarkId, gtsam::OrientedPlane3 value);

        const gtsam::Values& GetResults() const {return result;};

        const gtsam::Values& GetInitialValues() const {return initial;};

        const gtsam::NonlinearFactorGraph& GetFactorGraph();

        void createOdometryNoiseModel(gtsam::Vector6 odomVariance);

        void createOrientedPlaneNoiseModel(gtsam::Vector3 lmVariances);

    private:
        FactorGraphHandler fgh;
}