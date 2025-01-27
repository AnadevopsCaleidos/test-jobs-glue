import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


input_path = "s3://test-version-control-glue/versionContro"  
df = spark.read.format("csv").option("header", "true").load(input_path)  

#Prueba de conexion a github
df.show()


job.commit()