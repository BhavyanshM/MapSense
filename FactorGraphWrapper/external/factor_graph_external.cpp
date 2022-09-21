#pragma once

#include "factor_graph_external.h"

void FactorGraphExternal::AddPriorPoseFactor_Pose3(int index, float* pose)
{
    fgh.
}

void FactorGraphExternal::AddOdometryFactor_Pose3(float* odometry, int poseId)
{

}

void FactorGraphExternal::AddOrientedPlaneFactor_Vector4(float* lmMean, int lmId, int poseIndex)
{

}

void FactorGraphExternal::Optimize()
{

}

void FactorGraphExternal::OptimizeISAM2(uint8_t numberOfUpdates)
{

}

void FactorGraphExternal::ClearISAM2()
{

}

void FactorGraphExternal::SetPoseInitialValue_Pose3(int index, float* value)
{

}

void FactorGraphExternal::SetOrientedPlaneInitialValue_OrientedPlane3(int landmarkId, float* value)
{

}

void FactorGraphExternal::CreateOdometryNoiseModel_Vector6(float* odomVariance)
{

}

void FactorGraphExternal::CreateOrientedPlaneNoiseModel_Vector3(float* lmVariances)
{

}