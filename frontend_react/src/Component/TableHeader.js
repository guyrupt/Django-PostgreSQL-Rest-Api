import { Space } from 'antd'
import { DoubleRightOutlined } from '@ant-design/icons';


const TableHeader = ({ company, location, level, tag }) => {
    let company_name, location_name, level_name, tag_name
    if (company == null) {
        company_name = "All"
    }else{
        company_name = company
    }
    if (location == null) {
        location_name = "All"
    }else{
        location_name = location
    }
    if (level == null) {
        level_name = "All"
    }else{
        level_name = level
    }
    if (tag == null) {
        tag_name = "All"
    }else{
        tag_name = tag
    }
    return(
        <div className='table'>
            <Space className='table-header'>
                <h1>Company: </h1>
                <h2>{company_name}</h2>
                <h1>    /    </h1>
                <h1>Location: </h1>
                <h2>{location_name}</h2>
                <h1>    /    </h1>
                <h1>Level: </h1>
                <h2>{level_name}</h2>
                <h1>    /    </h1>
                <h1>Tag: </h1>
                <h2>{tag_name}</h2>
            </Space>
        </div>
    )
}

export default TableHeader