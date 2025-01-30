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


input_path = "s3://s3://version-control-glue-test/segundo-job.csv"  
df = spark.read.format("csv").option("header", "true").load(input_path)  

df.show()
job.commit()

#comentario de prueba 2