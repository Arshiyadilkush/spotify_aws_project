import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Album
Album_node1750725094516 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://aws-project-spotify-datewithdata/staging/albums.csv"], "recurse": True}, transformation_ctx="Album_node1750725094516")

# Script generated for node Artist
Artist_node1750725093383 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://aws-project-spotify-datewithdata/staging/artists.csv"], "recurse": True}, transformation_ctx="Artist_node1750725093383")

# Script generated for node Tracks
Tracks_node1750725095299 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://aws-project-spotify-datewithdata/staging/track.csv"], "recurse": True}, transformation_ctx="Tracks_node1750725095299")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1750725314362 = Join.apply(frame1=Album_node1750725094516, frame2=Artist_node1750725093383, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumArtist_node1750725314362")

# Script generated for node Join with Tracks
JoinwithTracks_node1750725464303 = Join.apply(frame1=Tracks_node1750725095299, frame2=JoinAlbumArtist_node1750725314362, keys1=["track_id"], keys2=["track_id"], transformation_ctx="JoinwithTracks_node1750725464303")

# Script generated for node Drop Fields
DropFields_node1750725594415 = DropFields.apply(frame=JoinwithTracks_node1750725464303, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1750725594415")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1750725594415, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1750725065796", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1750725733427 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1750725594415, connection_type="s3", format="glueparquet", connection_options={"path": "s3://aws-project-spotify-datewithdata/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1750725733427")

job.commit()