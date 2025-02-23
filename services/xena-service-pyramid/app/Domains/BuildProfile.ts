import { validString, validEnum } from './Validators'
import { v4 as uuidv4 } from 'uuid'

type ProfileStatus = 'ENABLED' | 'DISABLED' | 'DELETED'

type Configuration = {
  template: 'XENA_RA' | 'XENA_APEP'
}

export default class BuildProfile {
  public readonly id: string
  public readonly name: string
  public readonly description: string | null
  public readonly gitUrl: string
  public readonly config: Configuration
  public readonly status: ProfileStatus

  constructor (
    id: string | null,
    name: string,
    description: string | null,
    gitUrl: string,
    config: Configuration,
    status: ProfileStatus,
  ) {
    this.id = validString(id ?? uuidv4(), 'BAD_BUILD_PROFILE_ID', 'NON_EMPTY')
    this.name = validString(name, 'BAD_BUILD_PROFILE_NAME', 'NON_EMPTY')
    this.description = description ? validString(description, 'BAD_BUILD_PROFILE_DESCRIPTION', 'NON_EMPTY') : null
    this.gitUrl = validString(gitUrl, 'BAD_BUILD_PROFILE_GIT_URL', 'NON_EMPTY')
    this.config = config
    this.status = validEnum(status, ['ENABLED', 'DISABLED', 'DELETED'], 'BAD_BUILD_STATUS')
  }

  public static fromJSON = (json) => new BuildProfile(
      json.id,
      json.name,
      json.description,
      json.gitUrl,
      json.config,
      json.status,
    )
}