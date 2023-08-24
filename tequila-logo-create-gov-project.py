import argparse
from label_studio_sdk import Client


def setup(port: int, token: str):
    # Define the URL where Label Studio is accessible and the API key for your user account
    LABEL_STUDIO_URL = f"http://localhost:{port}"
    # Connect to the Label Studio API and check the connection
    ls = Client(url=LABEL_STUDIO_URL, api_key=token)
    ls.check_connection()

    project = ls.start_project(
        title="Government Logo Annotation",
        label_config="""
        <View>
        <Image name="image" value="$image" zoom="true"/>
        <Filter name="filter" toName="label" hotkey="shift+f" minlength="0" placeholder="Filter"/>
        <View whenTagName="label" whenChoiceValue="Car">
            <TextArea name="other-class" toName="image" editable="true" perRegion="true" required="false" rows="1" placeholder="Brand's name" />
        </View>
        <RectangleLabels name="label" toName="image">
        <Label value="MCOT / อสมท" />
        <Label value="The Embassy of the United States in Bangkok" />
        <Label value="กรมการพัฒนาชุมชน กระทรวงมหาดไทย" />
        <Label value="กรมกิจการสตรีและสถาบันครอบครัว" />
        <Label value="กรมข่าวทหารบก" />
        <Label value="กรมประชาสัมพันธ์" />
        <Label value="กรมพัฒนาธุรกิจการค้า" />
        <Label value="กรมส่งเสริมอุตสาหกรรม" />
        <Label value="กรมสอบสวนคดีพิเศษ" />
        <Label value="กรมสุขภาพจิต กระทรวงสาธารณสุข" />
        <Label value="กรมอนามัย กระทรวงสาธารณสุข" />
        <Label value="กระทรวงกลาโหม" />
        <Label value="กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์" />
        <Label value="กระทรวงทรัพยากรธรรมชาติและสิ่งแวดล้อม" />
        <Label value="กระทรวงยุติธรรม" />
        <Label value="กองทุนบำเหน็จบำนาญข้าราชการ สำนักงานใหญ่" />
        <Label value="กองบัญชาการฐานทัพเรือสัตหีบ" />
        <Label value="การท่องเที่ยวแห่งประเทศไทย" />
        <Label value="การทางพิเศษแห่งประเทศไทย" />
        <Label value="การประปานครหลวง สำนักงานใหญ่" />
        <Label value="การรถไฟแห่งประเทศไทย" />
        <Label value="คณะแพทยศาสตร์ศิริราชพยาบาล มหาวิทยาลัยมหิดล" />
        <Label value="คณะวิทยาการเรียนรู้และศึกษาศาสตร์ มหาวิทยาลัยธรรมศาสตร์" />
        <Label value="ตลาดหลักทรัพย์แห่งประเทศไทย" />
        <Label value="ธนาคารแห่งประเทศไทย" />
        <Label value="มหาวิทยาลัยศรีนครินทรวิโรฒ" />
        <Label value="สถาบันเพิ่มผลผลิตแห่งชาติ" />
        <Label value="สำนักข่าว กรมประชาสัมพันธ์" />
        <Label value="สำนักงานคณะกรรมการการรักษาความมั่นคงปลอดภัยไซเบอร์แห่งชาติ" />
        <Label value="สำนักงานคณะกรรมการการศึกษาขั้นพื้นฐาน" />
        <Label value="สำนักงานคณะกรรมการกิจการกระจายเสียง กิจการโทรทัศน์ และกิจการโทรคมนาคมแห่งชาติ" />
        <Label value="สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล" />
        <Label value="สำนักงานคณะกรรมการสุขภาพแห่งชาติ" />
        <Label value="สำนักงานนโยบายและแผนทรัพยากรธรรมชาติและสิ่งแวดล้อม" />
        <Label value="สำนักงานนโยบายและแผนพลังงาน" />
        <Label value="สำนักงานพัฒนาธุรกรรมทางอิเล็กทรอนิกส์" />
        <Label value="สำนักงานพัฒนารัฐบาลดิจิทัล (องค์การมหาชน)" />
        <Label value="สำนักงานส่งเสริมเศรษฐกิจดิจิทัล" />
        <Label value="สำนักสื่อสารความเสี่ยงและพัฒนาพฤติกรรมสุขภาพ กรมควบคุมโรค" />
        </RectangleLabels>
        </View>
        """,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--port", type=int, help="port number")
    parser.add_argument("--token", type=str, help="label studio token")

    args = parser.parse_args()
    setup(args.port, args.token)
    print("project has been set up successfully")
