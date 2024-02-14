bandit_model = sagemaker.model.Model(
    image_uri=vw_image_uri,
    role=role,
    name="vw-model-1",
    model_data=f"s3://{s3_bucket}/{model_path}",
    sagemaker_session=sage_session,
)
